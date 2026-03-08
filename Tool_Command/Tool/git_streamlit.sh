←
←
**完整操作手册**

---

**1. 检查 SSH 连接 GitHub**
```bash
ssh -T git@github.com
```

---

**2. 检查 gh 登录状态**
```bash
gh auth status
```

---

**3. 进入项目目录**
```bash
cd /Users/longe/Documents/projects/Mypersonal_language_trainer/files
```

---

**4. 创建 GitHub 仓库**
```bash
gh repo create 仓库名 --public
```

---

**5. 初始化并上传代码**
```bash
git init
git add .
git commit -m "init"
git remote add origin git@github.com:longe000id-star/仓库名.git
git push -u origin main
```

---

**6. 部署到 Streamlit Cloud**
```bash
open https://share.streamlit.io
```
→ Create app → 填写：
- Repository: `https://github.com/longe000id-star/仓库名`
- Branch: `main`
- Main file path: `app.py`
- App URL: `自定义名字`
→ Deploy

---

**7. 添加 API Key 到 Streamlit Secrets**
```bash
open https://share.streamlit.io
```
→ 找到 app → ⋮ → Settings → Secrets → 填入：
```toml
GROQ_API_KEY = "你的key"
```
→ Save

---

**8. 打开 App**
```bash
open https://你的名字.streamlit.app
```

---

**9. 日常修改并更新**
```bash
cd /Users/longe/Documents/projects/Mypersonal_language_trainer/files
# 修改 app.py
git add app.py
git commit -m "描述改了什么"
git push
```
→ 等 1-2 分钟，Streamlit 自动更新

---

**10. 常用链接**
```bash
open https://lingua-core.streamlit.app
open https://github.com/longe000id-star/lingua-core
open https://share.streamlit.io
open https://console.groq.com/keys
```
