←
←
cd ~/Desktop/my-new-project
git init
git add .
git commit -m "first commit"
gh repo create my-new-project --public --source=. --remote=origin --push
git remote set-url origin git@github.com:longe000id-star/my-new-project.git
git remote -v
git push -u origin main

# 1. 查看当前分支
git branch

# 2. 拉取远程更新
git fetch origin

# 3. 合并到本地分支（假设分支是 main）
git pull origin main

# 4. 如果你用的是 master 分支
git pull origin master

# 5. 查看状态确认同步完成
git status

# 如果你用的是 master 分支

