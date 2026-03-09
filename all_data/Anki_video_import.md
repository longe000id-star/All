[← Script_Index](../all_index/Script_Index.md) 
# Anki 视频导入指南

## 前提准备

### 1. 安装 AnkiConnect 插件
1. 打开 Anki
2. 工具 → 插件 → 获取插件
3. 输入代码：`2055492159`
4. 重启 Anki
5. 之后每次运行脚本时，**保持 Anki 在后台运行**

### 2. 安装 Python 依赖
```bash
pip install requests
```

---

## 第一步：准备视频文件

### 如果是 MKV 格式，先转换成 MP4
```bash
ffmpeg -i "电影.mkv" -c:v copy -c:a aac -b:a 192k "电影.mp4"
```
> ⚠️ 用 `-c copy` 可能导致无声，因为 MKV 的 DTS/TrueHD 音频 MP4 不支持，必须加 `-c:a aac` 重新编码音频。

### 切割成片段（每段3分钟）
```bash
#!/bin/bash
SOURCE="电影.mp4"
OUTPUT_DIR="片段"
SEGMENT=180      # 每段秒数
DURATION=8094    # 总时长秒数（用 ffprobe 查询）

mkdir -p "$OUTPUT_DIR"
start=0
i=0

while [ $start -lt $DURATION ]; do
  output=$(printf "$OUTPUT_DIR/片段_%03d.mp4" $i)
  ffmpeg -ss $start -i "$SOURCE" -t $SEGMENT -c copy "$output" -y -loglevel error
  start=$((start + SEGMENT))
  i=$((i + 1))
done
```

查询总时长：
```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "电影.mp4"
```

---

## 第二步：复制视频到 Anki media 文件夹

Anki media 文件夹路径（先确认你的用户名）：
```bash
ls ~/Library/Application\ Support/Anki2/
```
通常是 `Lorie` 或 `User 1`，完整路径为：
```
~/Library/Application Support/Anki2/<用户名>/collection.media
```

### 批量复制并重命名（加前缀）
```bash
python3 -c "
import os, shutil
src = '/path/to/片段'           # 改成你的片段文件夹
dst = os.path.expanduser('~/Library/Application Support/Anki2/Lorie/collection.media')
prefix = '电影名_'               # 改成你想要的前缀

for f in sorted(os.listdir(src)):
    if f.endswith('.mp4'):
        shutil.copy2(os.path.join(src, f), os.path.join(dst, prefix + f))
        print(f'✅ {prefix + f}')
"
```

### 重命名已在 media 的文件（修改前缀）
```bash
python3 -c "
import os
media = os.path.expanduser('~/Library/Application Support/Anki2/Lorie/collection.media')
for f in os.listdir(media):
    if '片段' in f:
        new = '新前缀_' + f
        os.rename(os.path.join(media, f), os.path.join(media, new))
        print(f'✅ {f} → {new}')
"
```

---

## 第三步：批量创建 Anki 卡片

保存为 `anki_import.py`，根据需要修改顶部变量：

```python
#!/usr/bin/env python3
import os
import requests

ANKI_CONNECT = "http://localhost:8765"
DECK = "电影储备::小妇人"          # Deck 名，:: 表示子 deck
MODEL = "VideoCard"               # 自定义 notetype 名
ANKI_MEDIA = os.path.expanduser("~/Library/Application Support/Anki2/Lorie/collection.media")
FILE_PREFIX = "小妇人_片段"        # media 里文件名的前缀

FRONT_TEMPLATE = """
<div class="title">{{Title}}</div>
<div class="video-wrap">{{Video}}</div>
<div class="path"
  onclick="navigator.clipboard.writeText('open \"$HOME/Library/Application Support/Anki2/Lorie/collection.media/{{Title}}.mp4\"')"
  style="cursor:pointer"
  title="点击复制 open 命令">
  📋 open "$HOME/Library/Application Support/Anki2/Lorie/collection.media/{{Title}}.mp4"
</div>
"""

BACK_TEMPLATE = "{{FrontSide}}<hr><div class='note'>{{Note}}</div>"

CSS = """
.card { font-family: -apple-system, sans-serif; background: #1a1a2e; color: #eee; text-align: center; padding: 20px; }
.title { font-size: 1.1em; color: #aaa; margin-bottom: 12px; }
.video-wrap video { width: 100%; max-width: 720px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
.path { color: #888; font-size: 0.8em; margin-top: 10px; word-break: break-all; }
"""

def anki_request(action, **params):
    payload = {"action": action, "version": 6, "params": params}
    response = requests.post(ANKI_CONNECT, json=payload, timeout=30)
    result = response.json()
    if result.get("error"):
        print(f"  ⚠️  错误: {result['error']}")
        return None
    return result.get("result")

# 创建 notetype（已存在则跳过）
existing_models = anki_request("modelNames")
if MODEL not in existing_models:
    print(f"🔧 创建 notetype: {MODEL}")
    anki_request("createModel",
        modelName=MODEL,
        inOrderFields=["Title", "Video", "Note"],
        css=CSS,
        cardTemplates=[{"Name": "Card 1", "Front": FRONT_TEMPLATE, "Back": BACK_TEMPLATE}]
    )
    print("✅ notetype 创建成功")
else:
    print("✅ notetype 已存在")

anki_request("createDeck", deck=DECK)
print(f"📁 Deck: {DECK}\n")

videos = sorted([f for f in os.listdir(ANKI_MEDIA) if f.startswith(FILE_PREFIX) and f.endswith(".mp4")])
total = len(videos)
print(f"🎬 找到 {total} 个视频\n")

for idx, video in enumerate(videos, 1):
    video_name = os.path.splitext(video)[0]
    print(f"[{idx}/{total}] {video} ...")
    note = {
        "deckName": DECK,
        "modelName": MODEL,
        "fields": {"Title": video_name, "Video": f'[sound:{video}]', "Note": ""},
        "options": {"allowDuplicate": False},
        "tags": ["小妇人"],
    }
    result = anki_request("addNote", note=note)
    print(f"  ✅ 成功 (id: {result})" if result else "  ❌ 失败（可能重复）")

print(f"\n🎉 完成！共 {total} 个视频")
```

运行：
```bash
python3 anki_import.py
```

---

## 第四步：在 Anki 中查看视频

卡片正面会显示：
- 视频播放器（直接播放）
- 路径栏（点击复制 `open` 命令）

在 Terminal 打开视频文件：
```bash
open "$HOME/Library/Application Support/Anki2/Lorie/collection.media/小妇人_片段_000.mp4"
```

---

## 常见问题

### 连接 Anki 失败
- 确认 Anki 正在运行
- 确认 AnkiConnect 插件已启用（工具 → 插件）
- 测试连接：`curl http://localhost:8765`

### 视频没有声音
原始 MKV 音频格式不兼容，转换时加上音频重编码：
```bash
ffmpeg -i "电影.mkv" -c:v copy -c:a aac -b:a 192k "电影.mp4"
```

### 卡片显示重复错误
卡片已存在，不影响使用，忽略即可。如需重新导入，先在 Anki 里删除对应 deck。

### QuickTime 没有声音
如果 MP4 有 AAC 音频但 QuickTime 仍然没声音，可能是 6声道（5.1环绕声）的问题，把音频降到2声道：
```bash
ffmpeg -i 输入.mp4 -c:v copy -c:a aac -ac 2 输出.mp4
```
用 VLC 可以正常播放6声道，推荐用 VLC 代替 QuickTime。

### 查看文件头尾内容
```bash
head -3 文件名.md  # 查看文件开头3行
tail -3 文件名.md  # 查看文件倒数3行
```

```bash
tail -3 文件名.md  # 查看文件倒数3行
```

### Anki 卡顿
视频文件较大（100MB+）时 Anki 渲染会慢。
> ⚠️ 不要用脚本通过 base64 上传视频给 AnkiConnect，100MB+ 的文件编码后会更大，传输极慢。**正确做法是直接用 `shutil.copy` 把文件复制到 media 文件夹（秒完），再用 AnkiConnect 只负责创建卡片。**

如果仍然卡顿，可以压缩视频后再复制到 media：
```bash
mkdir -p 压缩
for f in 片段/*.mp4; do
  ffmpeg -i "$f" -vf scale=960:-2 -crf 28 -preset fast "压缩/$(basename $f)"
done
```

[← Script_Index](../all_index/Script_Index.md) 

###### Backup
```markdown
[← Script_Index](../all_index/Script_Index.md) 
```