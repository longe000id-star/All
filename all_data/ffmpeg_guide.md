[← Terminal_Index](Terminal_Index.md)


# ffmpeg 视频处理操作指南 (Fish Shell 版)

本文档包含适用于 **Fish Shell** 的 ffmpeg 命令，可直接复制到终端中使用。

> **注意**：Fish Shell 的语法与 Bash 不同，特别是循环和变量引用方式。

## 一、安装 ffmpeg

**macOS 安装**

```fish
brew install ffmpeg
```

**检查是否安装成功**

```fish
ffmpeg -version
```

## 二、格式转换

**AVI 转 MP4**

```fish
ffmpeg -i "输入文件.avi" "输出文件.mp4"
```

**MP4 转 MKV**

```fish
ffmpeg -i "输入文件.mp4" "输出文件.mkv"
```

**MKV 转 MP4（不重新编码，速度极快，画质无损）**

```fish
ffmpeg -i "输入文件.mkv" -c copy "输出文件.mp4"
```

**批量转换：当前目录所有 .avi 文件转 .mp4 (Fish Shell 语法)**

```fish
for f in *.avi
    ffmpeg -i "$f" (basename "$f" .avi).mp4
end
```

或使用更简洁的写法：

```fish
for f in *.avi; ffmpeg -i "$f" (basename "$f" .avi).mp4; end
```

## 三、按时间剪辑 ★ 重点

**每 3 分钟自动切一段（180秒）**

输出自动编号：`片段_000.mp4`、`片段_001.mp4` ...

```fish
ffmpeg -i "输入文件.mp4" \
  -f segment \
  -segment_time 180 \
  -c copy \
  "片段_%03d.mp4"
```

**常用时长对照：**

- 1 分钟 → segment_time 60
- 2 分钟 → segment_time 120
- 3 分钟 → segment_time 180
- 5 分钟 → segment_time 300
- 10 分钟 → segment_time 600
- 15 分钟 → segment_time 900
- 30 分钟 → segment_time 1800

**手动指定时间点剪辑**

从第1分钟剪到第5分钟：

```fish
ffmpeg -i "输入.mp4" -ss 00:01:00 -to 00:05:00 -c copy "片段.mp4"
```

从第30秒开始，剪取3分钟：

```fish
ffmpeg -i "输入.mp4" -ss 00:00:30 -t 00:03:00 -c copy "片段.mp4"
```

参数说明：
- `-ss` 开始时间（HH:MM:SS）
- `-to` 结束时间（HH:MM:SS）
- `-t` 持续时长（HH:MM:SS）

**关键词定位剪辑**（需要字幕文件 .srt）

第1步：搜索字幕文件中的关键词，找到时间点：

```fish
grep -n "关键词" 字幕文件.srt
```

输出示例：
```
245: 00:12:34,000 --> 00:12:38,000
246: 关键词出现在这里
```

第2步：以关键词时间点为中心，前后各 1.5 分钟剪辑（关键词在 00:12:34 → 开始时间 00:11:04，结束时间 00:14:04）：

```fish
ffmpeg -i "输入.mp4" -ss 00:11:04 -to 00:14:04 -c copy "关键词片段.mp4"
```

没有字幕？用 Whisper 自动生成：

```fish
whisper "输入.mp4" --language Chinese
```

## 四、字幕处理

**查看字幕类型**（软字幕 or 硬字幕）

有 "Stream #0:x: Subtitle" → 软字幕，可以去掉；没有 Subtitle 行 → 硬字幕，烧进画面，无法去除：

```fish
ffprobe -i "输入文件.mkv"
```

**去掉软字幕**

```fish
ffmpeg -i "输入.mkv" -sn -c copy "无字幕.mkv"
```

**提取字幕为 .srt 文件**

```fish
ffmpeg -i "输入.mkv" -map 0:s:0 "字幕.srt"
```

**将外部 .srt 字幕烧录进视频（硬字幕）**

```fish
ffmpeg -i "输入.mp4" -vf subtitles="字幕.srt" "带字幕.mp4"
```

## 五、压缩与画质

**压缩视频**（CRF：18=高画质大文件，28=低画质小文件，推荐 23）

```fish
ffmpeg -i "输入.mp4" -crf 23 "压缩后.mp4"
```

**转为 1080p**

```fish
ffmpeg -i "输入.mp4" -vf scale=1920:1080 "1080p.mp4"
```

**转为 720p**

```fish
ffmpeg -i "输入.mp4" -vf scale=1280:720 "720p.mp4"
```

**转为 480p**

```fish
ffmpeg -i "输入.mp4" -vf scale=854:480 "480p.mp4"
```

## 六、音频处理

**提取音频**

```fish
ffmpeg -i "输入.mp4" -vn "音频.mp3"
```

**去掉音频**

```fish
ffmpeg -i "输入.mp4" -an "无音频.mp4"
```

**替换音频**

```fish
ffmpeg -i "视频.mp4" -i "音频.mp3" -c:v copy -map 0:v -map 1:a "合并.mp4"
```

**调整音量**（2.0 = 双倍音量）

```fish
ffmpeg -i "输入.mp4" -af "volume=2.0" "输出.mp4"
```

## 七、其他实用功能

**截图**（在第1分30秒）

```fish
ffmpeg -i "输入.mp4" -ss 00:01:30 -frames:v 1 "截图.jpg"
```

**每隔10秒截一张图**

```fish
ffmpeg -i "输入.mp4" -vf "fps=1/10" "截图_%04d.jpg"
```

**2倍速**

```fish
ffmpeg -i "输入.mp4" -vf "setpts=0.5*PTS" -af "atempo=2.0" "2x.mp4"
```

**0.5倍速（慢放）**

```fish
ffmpeg -i "输入.mp4" -vf "setpts=2.0*PTS" -af "atempo=0.5" "0.5x.mp4"
```

**合并多个视频 (Fish Shell 语法)**

```fish
echo "file '片段_000.mp4'" > filelist.txt
echo "file '片段_001.mp4'" >> filelist.txt
echo "file '片段_002.mp4'" >> filelist.txt
ffmpeg -f concat -safe 0 -i filelist.txt -c copy "合并后.mp4"
```

**旋转视频**（顺时针90°）

```fish
ffmpeg -i "输入.mp4" -vf "transpose=1" "旋转后.mp4"
```

transpose 参数说明：
- `transpose=0`: 逆时针90°
- `transpose=1`: 顺时针90°
- `transpose=2`: 逆时针90°+垂直翻转
- `transpose=3`: 顺时针90°+垂直翻转

## 八、快速参考

| 操作 | 命令 |
|------|------|
| 格式转换 | `ffmpeg -i 输入.avi 输出.mp4` |
| 3分钟切片 | `ffmpeg -i 输入.mp4 -f segment -segment_time 180 -c copy 片段_%03d.mp4` |
| 手动剪辑 | `ffmpeg -i 输入.mp4 -ss 00:01:00 -to 00:05:00 -c copy 片段.mp4` |
| 去掉字幕 | `ffmpeg -i 输入.mkv -sn -c copy 无字幕.mkv` |
| 提取音频 | `ffmpeg -i 输入.mp4 -vn 音频.mp3` |
| 去掉音频 | `ffmpeg -i 输入.mp4 -an 无音频.mp4` |
| 压缩视频 | `ffmpeg -i 输入.mp4 -crf 28 压缩后.mp4` |
| 转720p | `ffmpeg -i 输入.mp4 -vf scale=1280:720 720p.mp4` |
| 截图 | `ffmpeg -i 输入.mp4 -ss 00:01:30 -frames:v 1 截图.jpg` |
| 2倍速 | `ffmpeg -i 输入.mp4 -vf "setpts=0.5*PTS" -af "atempo=2.0" 2x.mp4` |
| 查看视频信息 | `ffprobe -i 输入.mp4` |
| 批量转换 (Fish) | `for f in *.avi; ffmpeg -i "$f" (basename "$f" .avi).mp4; end` |
