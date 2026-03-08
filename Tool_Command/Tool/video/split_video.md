[← Terminal_Index](../../Terminal_Index.md)

我说的是这个：：：我说的是这个：
#!/bin/bash

SOURCE="/Users/longe/Downloads/悲惨世界.mkv"

MP4="/Users/longe/Downloads/悲惨世界.mp4"
OUTPUT_DIR="/Users/longe/Downloads/片段"
SEGMENT=180   # 每段秒数（3分钟=180秒）
DURATION=8094 # 总时长秒数（2小时14分54秒）


# 第二步：创建输出文件夹，清理旧片段
mkdir -p "$OUTPUT_DIR"

echo "⏳ 第二步：开始切割，共约 $((DURATION / SEGMENT + 1)) 个片段..."

start=0
i=0

while [ $start -lt $DURATION ]; do
  output=$(printf "$OUTPUT_DIR/悲惨世界_片段_%03d.mp4" $i)
  echo "▶ 正在切割片段 $i（开始时间：${start}秒）..."
  ffmpeg -ss $start \
    -i "$MP4" \
    -t $SEGMENT \
    -c copy \
    "$output" -y -loglevel error
  start=$((start + SEGMENT))
  i=$((i + 1))
done

echo "✅ 完成！共切割 $i 个片段，保存在：$OUTPUT_DIR"
