
[← Terminal_Index](Terminal_Index.md)

# Terminal 常用操作指南（fish shell）

---

## 1. 批量改名

### 用 sed 替换文件内容中的字符串
```bash
sed -i '' 's|旧字符串|新字符串|' 文件名.sh
```
例如修复路径拼写错误：
```bash
sed -i '' 's|Dowloads|Downloads|' split_video.sh
```
替换多处：
```bash
sed -i '' 's|-c copy "$MP4"|-c:v copy -c:a aac -b:a 192k "$MP4"|' split_video.sh
```

### 用 Python 批量重命名文件
```python
python3 -c "
import os
media = os.path.expanduser('~/Library/Application Support/Anki2/Lorie/collection.media')
for f in os.listdir(media):
    if '片段' in f:
        new = '悲惨世界_' + f
        os.rename(os.path.join(media, f), os.path.join(media, new))
        print(f'✅ {f} → {new}')
"
```

修改前缀（替换已有前缀）：
```python
python3 -c "
import os
media = os.path.expanduser('~/Library/Application Support/Anki2/Lorie/collection.media')
for f in os.listdir(media):
    if f.startswith('旧前缀_'):
        new = f.replace('旧前缀_', '新前缀_', 1)
        os.rename(os.path.join(media, f), os.path.join(media, new))
        print(f'✅ {f} → {new}')
"
```

---

## 2. 搜索特定文件

### 按文件名搜索
```bash
find ~/Downloads -name "*.mkv" 2>/dev/null
find ~/Downloads -name "悲惨世界*" 2>/dev/null
```

### 在某目录下过滤文件名（grep）
```bash
ls ~/Library/Application\ Support/Anki2/Lorie/collection.media/ | grep 片段
ls ~/Downloads/片段/ | grep 悲惨世界
```

### 路径含空格时用引号或转义
```bash
# 方法1：双引号 + $HOME（推荐）
ls "$HOME/Library/Application Support/Anki2/Lorie/collection.media/"

# 方法2：反斜杠转义
ls ~/Library/Application\ Support/Anki2/Lorie/collection.media/
```
> ⚠️ fish shell 中 `~` 在双引号里不展开，必须用 `$HOME` 代替

---

## 3. 更改代码（sed 行内替换）

### 替换文件中的字符串
```bash
sed -i '' 's|原内容|新内容|' 文件名
```

### 确认修改是否生效
```bash
grep "关键字" 文件名
cat 文件名
```

### 例子：修改脚本中的 ffmpeg 参数
```bash
sed -i '' 's|-c copy "$MP4"|-c:v copy -c:a aac -b:a 192k "$MP4"|' split_video.sh
grep "c:a" split_video.sh   # 验证是否改成功
```

---

## 4. 查看实时进度

### 监控文件大小变化（判断是否还在写入）
```bash
# fish shell 语法
while true; ls -lh ~/Downloads/悲惨世界.mp4 2>/dev/null; sleep 3; end
```

### 监控文件数量变化（判断切割进度）
```bash
while true; echo (ls ~/Downloads/片段/ | wc -l) 个片段; sleep 3; end
```

### 监控端口连接（判断服务是否在运行）
```bash
while true; lsof -i :8765 | wc -l; sleep 2; end
```

> ⚠️ fish shell 没有 `watch` 命令，用 `while true; ...; sleep N; end` 代替
> 按 `Ctrl+C` 退出循环

---

## 5. 打开文件 / 文件夹

### 用系统默认程序打开文件
```bash
open "$HOME/Library/Application Support/Anki2/Lorie/collection.media/小妇人_片段_000.mp4"
```

### 在 Finder 中打开文件夹
```bash
open "$HOME/Library/Application Support/Anki2/Lorie/collection.media"
```

### 路径含空格时必须用 `$HOME` + 双引号
```bash
# ✅ 正确
open "$HOME/Library/Application Support/Anki2/Lorie/collection.media"

# ❌ 错误（~ 在双引号里不展开）
open "~/Library/Application Support/Anki2/Lorie/collection.media"

# ❌ 错误（空格会被解析成多个参数）
open ~/Library/Application Support/Anki2/Lorie/collection.media
```

### 在 Finder 中前往文件夹（GUI 方式）
Finder → 菜单栏「前往」→「前往文件夹」→ 粘贴路径：
```
~/Library/Application Support/Anki2/Lorie/collection.media
```
