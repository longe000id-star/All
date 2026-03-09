#!/usr/bin/env python3
import os
import requests

ANKI_CONNECT = "http://localhost:8765"
DECK = "电影储备:: 悲惨世界"
MODEL = "VideoCard"
ANKI_MEDIA = os.path.expanduser("~/Library/Application Support/Anki2/Lorie/collection.media")

FRONT_TEMPLATE = """
<div class="title">{{Title}}</div>
<div class="video-wrap">{{Video}}</div>
<div class="path">📁 ~/Library/Application Support/Anki2/Lorie/collection.media/{{Title}}.mp4</div>
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

# 确保 deck 存在
anki_request("createDeck", deck=DECK)
print(f"📁 Deck: {DECK}\n")

# 直接读 media 里的小妇人_片段_xxx.mp4
videos = sorted([f for f in os.listdir(ANKI_MEDIA) if f.startswith("悲惨世界_片段") and f.endswith(".mp4")])
total = len(videos)
print(f"🎬 找到 {total} 个视频\n")

for idx, video in enumerate(videos, 1):
    video_name = os.path.splitext(video)[0]  # 小妇人_片段_000

    print(f"[{idx}/{total}] {video} ...")

    note = {
        "deckName": DECK,
        "modelName": MODEL,
        "fields": {
            "Title": video_name,
            "Video": f'[sound:{video}]',
            "Note": "",
        },
        "options": {"allowDuplicate": False},
        "tags": ["小妇人"],
    }

    result = anki_request("addNote", note=note)
    if result:
        print(f"  ✅ 卡片成功 (id: {result})")
    else:
        print(f"  ❌ 卡片失败（可能重复）")

print(f"\n🎉 完成！共 {total} 个视频")
