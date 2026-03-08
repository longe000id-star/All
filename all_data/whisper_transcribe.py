"""
[← Script_Index](../../Script_Index.md)
"""
#!/usr/bin/env python3
import os
import whisper

MEDIA_DIR = os.path.expanduser("~/Library/Application Support/Anki2/Lorie/collection.media")
OUTPUT_DIR = os.path.expanduser("~/Downloads/字幕")
os.makedirs(OUTPUT_DIR, exist_ok=True)

videos = sorted([
    f for f in os.listdir(MEDIA_DIR)
    if f.startswith("悲惨世界_片段") and f.endswith(".mp4")
])
total = len(videos)
print(f"🎬 找到 {total} 个片段（跳过损坏文件）\n")

print("⏳ 加载 Whisper 模型...")
model = whisper.load_model("base")
print("✅ 模型加载完成\n")

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

success = 0
failed = []

for idx, video in enumerate(videos, 1):
    video_path = os.path.join(MEDIA_DIR, video)
    name = os.path.splitext(video)[0]
    srt_path = os.path.join(OUTPUT_DIR, name + ".srt")

    if os.path.exists(srt_path):
        print(f"[{idx}/{total}] ⏭️  已存在: {name}.srt")
        success += 1
        continue

    print(f"[{idx}/{total}] 🎙️  转录: {video} ...")
    try:
        result = model.transcribe(video_path, language="en")
        with open(srt_path, "w") as f:
            for i, seg in enumerate(result["segments"], 1):
                start = format_time(seg["start"])
                end = format_time(seg["end"])
                f.write(f"{i}\n{start} --> {end}\n{seg['text'].strip()}\n\n")
        print(f"  ✅ 完成")
        success += 1
    except Exception as e:
        print(f"  ❌ 失败: {e}")
        failed.append(video)

print(f"\n🎉 完成！成功 {success} 个，失败 {len(failed)} 个")
if failed:
    print("失败文件：")
    for f in failed:
        print(f"  - {f}")
