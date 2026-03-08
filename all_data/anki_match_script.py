"""
[← Script_Index](../../Script_Index.md)
"""

#!/usr/bin/env python3
import os
import re
import requests
import pdfplumber

ANKI_CONNECT = "http://localhost:8765"

DECK = "电影储备::悲惨世界"
PDF_PATH = "/Users/longe/Downloads/les-miserables-2012.pdf"
SRT_DIR = os.path.expanduser("~/Downloads/字幕")
REST_FILE = os.path.expanduser("~/Downloads/rest.txt")


def anki_request(action, **params):
    payload = {"action": action, "version": 6, "params": params}
    response = requests.post(ANKI_CONNECT, json=payload, timeout=30)
    result = response.json()
    if result.get("error"):
        print(f"  ⚠️  错误: {result['error']}")
        return None
    return result.get("result")

def parse_srt_lines(path):
    """解析SRT文件，返回所有字幕文本行"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        try:
            with open(path, 'r', encoding='latin-1') as f:
                content = f.read()
        except:
            return []
    
    blocks = re.split(r'\n\n+', content.strip())
    lines = []
    for block in blocks:
        parts = block.strip().split('\n')
        if len(parts) >= 3:
            # 合并所有文本行
            text = ' '.join(parts[2:]).strip()
            # 清理HTML标签
            text = re.sub(r'<[^>]+>', '', text)
            text = re.sub(r'{\\an\d}', '', text)
            # 只保留文本，去掉特殊符号
            text = re.sub(r'[^\w\s\u4e00-\u9fff\']', ' ', text)
            # 合并多个空格
            text = re.sub(r'\s+', ' ', text)
            if text and len(text.split()) >= 2:  # 至少2个词
                lines.append(text.strip().lower())
    return lines

def find_line_in_script(line, script_text, start_pos, window=8000):
    """
    在剧本中找句子（模糊匹配）
    返回找到的位置，找不到返回-1
    """
    if start_pos >= len(script_text):
        return -1
    
    # 清理句子：去掉所有非字母数字字符，转小写
    clean_line = re.sub(r'[^\w\s\']', '', line.lower())
    words = clean_line.split()
    
    if len(words) < 2:
        return -1
    
    # 取前3个词和后3个词作为搜索关键词
    start_key = ' '.join(words[:3])
    end_key = ' '.join(words[-3:])
    
    # 搜索窗口（从start_pos开始，往后找window个字符）
    end_pos = min(start_pos + window, len(script_text))
    search_area = script_text[start_pos:end_pos].lower()
    
    # 先找前3个词
    idx = search_area.find(start_key)
    if idx != -1:
        # 找到了，检查这个位置附近是否有后3个词
        context = search_area[idx:idx+len(line)+200]
        if end_key in context:
            return start_pos + idx
    
    # 如果没找到，尝试只找后3个词
    idx = search_area.find(end_key)
    if idx != -1:
        return start_pos + idx
    
    # 还是没找到，尝试找任意2个连续的关键词
    for i in range(len(words)-1):
        phrase = ' '.join(words[i:i+2])
        idx = search_area.find(phrase)
        if idx != -1:
            return start_pos + idx
    
    return -1

def extract_script_text(pdf_path):
    """提取剧本全文"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = []
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
            return '\n'.join(text)
    except Exception as e:
        print(f"❌ 读取PDF失败: {e}")
        return ""

print("📖 加载剧本全文...")
script = extract_script_text(PDF_PATH)
if not script:
    print("❌ 无法读取剧本，退出")
    exit(1)

script_start = script.find('BLACK SCREEN')
if script_start == -1:
    script_start = 0
script = script[script_start:]
print(f"✅ 剧本共 {len(script)} 字符（从BLACK SCREEN开始）")

print(f"✅ 剧本共 {len(script)} 字符\n")

# 获取所有片段文件
media_dir = os.path.expanduser("~/Library/Application Support/Anki2/Lorie/collection.media")
all_segments = []
if os.path.exists(media_dir):
    all_segments = sorted([
        os.path.splitext(f)[0]
        for f in os.listdir(media_dir)
        if f.startswith("悲惨世界_片段") and f.endswith(".mp4")
    ], key=lambda x: int(x.split('_')[-1]))
total = len(all_segments)
print(f"📹 找到 {total} 个视频片段\n")

# 每个片段平均占剧本多少字符
default_step = len(script) // total if total > 0 else 3000

print("🔗 自上而下搜索...\n")
segment_ranges = {}
cursor = 0

# 第一遍：处理所有非跳过的片段
print("📌 处理所有片段...")
for seg in all_segments:
        
    start_idx = cursor
    print(f"\n📹 {seg} 起始: {start_idx}")

    srt_path = os.path.join(SRT_DIR, seg + ".srt")
    if not os.path.exists(srt_path):
        end_idx = start_idx + default_step
        segment_ranges[seg] = (start_idx, end_idx)
        cursor = end_idx
        print(f"  ⚠️  无字幕文件，使用默认步长: {start_idx}-{end_idx}")
        continue

    lines = parse_srt_lines(srt_path)
    if not lines or len(lines) < 5:
        end_idx = start_idx + default_step
        segment_ranges[seg] = (start_idx, end_idx)
        cursor = end_idx
        print(f"  ⚠️  字幕不足5行，使用默认步长: {start_idx}-{end_idx}")
        continue

    print(f"  字幕总行数: {len(lines)}")
    
    # 取倒数5句
    last5 = lines[-5:]
    print(f"  倒数5句:")
    
    # 找最后一句话的位置
    last_line = last5[-1]  # 倒数第1句
    last_pos = find_line_in_script(last_line, script, start_idx)
    
    if last_pos != -1:
        print(f"  ✅ 找到最后一句位置: {last_pos}")
        print(f"    最后一句: {last_line[:50]}...")
        
        # 结束位置 = 最后一句的位置 + 300
        end_idx = last_pos + 300
        end_idx = min(end_idx, len(script))
        
        print(f"  ✅ {seg}: {start_idx}-{end_idx}")
    else:
        # 如果找不到最后一句，尝试找倒数第2句
        second_last = last5[-2]
        last_pos = find_line_in_script(second_last, script, start_idx)
        if last_pos != -1:
            print(f"  ✅ 找到倒数第2句位置: {last_pos}")
            end_idx = last_pos + 300
            end_idx = min(end_idx, len(script))
            print(f"  ✅ {seg}: {start_idx}-{end_idx}")
        else:
            print(f"  ⚠️  找不到匹配，使用默认步长")
            end_idx = start_idx + default_step
    
    segment_ranges[seg] = (start_idx, end_idx)
    cursor = end_idx
    print(f"  ➡️  新光标: {cursor}")


# 找出未被覆盖的剧本段落
print("\n📝 分析未覆盖的剧本内容...")
covered = sorted([r for r in segment_ranges.values() if r and isinstance(r, tuple)])
rest_chunks = []
prev_pos = 0

for start, end in covered:
    if start > prev_pos + 1000:  # 间隙大于1000字符
        chunk = script[prev_pos:start].strip()
        if len(chunk) > 500:
            rest_chunks.append((prev_pos, start, chunk))
            print(f"  发现未覆盖段落: {prev_pos}-{start} ({len(chunk)} 字符)")
    prev_pos = max(prev_pos, end)

if prev_pos < len(script) - 1000:
    chunk = script[prev_pos:].strip()
    if len(chunk) > 500:
        rest_chunks.append((prev_pos, len(script), chunk))
        print(f"  发现末尾未覆盖段落: {prev_pos}-{len(script)} ({len(chunk)} 字符)")

if rest_chunks:
    with open(REST_FILE, 'w', encoding='utf-8') as f:
        f.write(f"未覆盖内容（共 {len(rest_chunks)} 段）:\n\n")
        for i, (s, e, chunk) in enumerate(rest_chunks, 1):
            f.write(f"{'='*60}\n")
            f.write(f"[段落 {i}] 字符 {s}-{e} (长度: {e-s})\n")
            f.write(f"{'='*60}\n")
            f.write(f"{chunk[:1000]}\n\n")
    print(f"\n📝 已写入: {REST_FILE}")

# 更新 Anki 卡片
print("\n🃏 更新 Anki 卡片...")
note_ids = anki_request("findNotes", query=f'deck:"{DECK}"')
if note_ids:
    notes_info = anki_request("notesInfo", notes=note_ids)
    if notes_info:
        updated_count = 0
        for note in notes_info:
            title = note['fields']['Title']['value']
            r = segment_ranges.get(title)
            if not r:
                continue
            
            content = script[r[0]:r[1]].strip()
            if not content:
                print(f"  ⚠️  {title}: 内容为空")
                continue
            
            content_escaped = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            
            # 与例子完全一致：使用class而不是内联样式
            html = f'<div class="scene-content">{content_escaped}</div>'
            
            result = anki_request("updateNoteFields", note={
                "id": note['noteId'],
                "fields": {"Note": html}
            })
            if result is not None:
                updated_count += 1
                print(f"  ✅ {title}: {len(content)} 字符")
        
        print(f"\n✅ 更新 {updated_count}/{len(notes_info)} 张卡片")

print("\n📊 最终统计:")
total_covered = 0
for seg in sorted(segment_ranges.keys(), key=lambda x: int(x.split('_')[-1])):
    r = segment_ranges[seg]
    if r:
        length = r[1]-r[0]
        total_covered += length
        print(f"  {seg}: {r[0]}-{r[1]} ({length} chars)")
    else:
        print(f"  {seg}: 未处理")

print(f"\n📊 总覆盖: {total_covered}/{len(script)} 字符 ({total_covered/len(script)*100:.1f}%)")
print(f"\n🎉 完成！")
