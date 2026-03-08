[← AI_Index](../../AI_Index.md) 

# Claude 容器目录 & 工具完整指南

---

## 一、容器目录结构

### 📂 `/mnt/user-data/` — 用户数据区

| 目录 | 权限 | 说明 |
|---|---|---|
| `uploads/` | 只读 | 你上传的文件自动出现在这里，Claude 可以读取 |
| `outputs/` | 可写 | Claude 把最终文件放这里，你才能下载 |
| `tool_results/` | 系统 | 工具调用的中间结果，系统内部使用，无需关心 |

**提示词写法：**
> "把所有输出文件保存到 `/mnt/user-data/outputs/` 并用 `present_files` 给我下载链接"

**Claude 会做什么不同：**
不加这句，Claude 可能只把文件放在 `/home/claude/` 工作区，你看不到。加了之后 Claude 会强制把文件移到 `outputs/` 并调用 `present_files`。

---

### 📂 `/mnt/skills/` — 技能库（只读）

Claude 在执行特定任务前会主动读取对应的 SKILL.md 文件，获取最佳实践。

| 目录 | 说明 |
|---|---|
| `public/docx/` | 生成高质量 Word 文档的指南 |
| `public/pdf/` | 生成/处理 PDF 的指南 |
| `public/pptx/` | 生成 PowerPoint 的指南 |
| `public/xlsx/` | 生成 Excel 的指南 |
| `public/frontend-design/` | 前端 UI 设计的最佳实践 |
| `public/product-self-knowledge/` | Anthropic 产品知识指南 |
| `examples/algorithmic-art/` | 算法艺术生成示例 |
| `examples/skill-creator/` | 创建新技能的工具 |
| `examples/mcp-builder/` | 构建 MCP 连接器的工具 |
| `examples/canvas-design/` | Canvas 设计示例 |
| `examples/theme-factory/` | 主题生成示例 |
| `examples/web-artifacts-builder/` | Web Artifact 构建示例 |
| `examples/slack-gif-creator/` | Slack GIF 创建示例 |
| `examples/brand-guidelines/` | 品牌指南示例 |
| `examples/internal-comms/` | 内部沟通模板示例 |
| `examples/doc-coauthoring/` | 文档协作示例 |
| `examples/benepass-reimbursement/` | 报销流程示例 |

**提示词写法：**
> "生成这个文件之前，先读取对应的 SKILL.md"

**Claude 会做什么不同：**
Claude 默认会主动读取，但加了这句可以强制提醒，确保 Claude 不跳过这一步，输出质量更高。

---

### 📂 `/home/claude/` — Claude 工作区（临时）

| 说明 |
|---|
| Claude 的临时工作目录，用于中间处理、测试、编译等 |
| 你看不到这里的文件 |
| 对话结束后自动重置清空 |
| 预装了 Python、Node.js、npm、pip 等工具 |

**提示词写法：**
> "所有脚本先保存成文件再执行，不要用 `python3 -c` 直接运行"

**Claude 会做什么不同：**
默认情况下 Claude 常用 `python3 -c "..."` 内存执行，不生成文件。加了这句后 Claude 会先 `create_file` 保存脚本，再执行，你可以拿到所有中间脚本。

---

### 📂 `/mnt/transcripts/` — 对话记录（只读）

| 说明 |
|---|
| 系统内部使用，存储对话记录 |
| Claude 可读取，但你无法直接访问 |

---

## 二、工具完整列表

### 🗂️ 文件操作类

| 工具 | 说明 | 提示词写法 | Claude 会做什么不同 |
|---|---|---|---|
| `create_file` | 创建新文件并写入内容 | "把代码保存成文件" | 生成可下载的实体文件，而不是只在聊天里显示代码 |
| `str_replace` | 精确替换文件中某段内容 | "修改文件里的 X 部分" | 对已有文件做精准编辑，不重写整个文件 |
| `view` | 查看文件内容或目录结构 | "先看一下文件结构再开始" | Claude 会先读文件再操作，避免盲目修改 |
| `present_files` | 把 outputs/ 里的文件暴露为下载链接 | "给我所有生成文件的下载链接" | 每次回答结束时主动提供下载，而不是只说"文件已生成" |
| `bash_tool` | 在容器里执行任意 bash 命令 | "用命令行执行/安装/测试" | 可以运行脚本、安装包、编译代码、批量处理文件等 |

---

### 🌐 网络搜索类

| 工具 | 说明 | 提示词写法 | Claude 会做什么不同 |
|---|---|---|---|
| `web_search` | 用搜索引擎搜索网络 | "搜索最新的..." | 获取知识截止日期后的最新信息 |
| `web_fetch` | 获取指定 URL 的完整页面内容 | "帮我读这个网址：..." | 获取完整页面正文，而不只是搜索摘要 |
| `image_search` | 搜索并返回图片 | "给我看一些...的图片" | 在回答中内嵌相关图片 |

---

### 🗺️ 地图与位置类

| 工具 | 说明 | 提示词写法 | Claude 会做什么不同 |
|---|---|---|---|
| `places_search` | 搜索地点、餐厅、景点等 | "帮我找附近的..." | 返回真实地点数据（评分、地址、营业时间） |
| `places_map_display_v0` | 在地图上展示地点或行程 | "把这些地点显示在地图上" | 生成可交互地图，而不只是文字列表 |
| `weather_fetch` | 获取某地实时天气 | "X地现在天气怎么样" | 返回实时天气数据 |

---

### 📊 内容展示类

| 工具 | 说明 | 提示词写法 | Claude 会做什么不同 |
|---|---|---|---|
| `recipe_display_v0` | 显示可动态调整份量的食谱 | "给我一个食谱" | 生成可交互食谱组件，可以拖动调整份量 |
| `message_compose_v1` | 起草邮件/短信/Slack消息 | "帮我写一封邮件给..." | 生成多个策略版本供选择，附发送按钮 |
| `ask_user_input_v0` | 向你提问，显示为可点击按钮 | （Claude 主动使用） | 把问题变成按钮选项，而不是让你打字回答 |
| `fetch_sports_data` | 获取体育赛事实时数据 | "XX比赛现在比分是多少" | 返回实时比分、排名、球员数据 |

---

### 🔌 第三方连接类

| 工具 | 说明 | 提示词写法 | Claude 会做什么不同 |
|---|---|---|---|
| `search_mcp_registry` | 搜索可用的外部应用连接器 | "帮我连接 Google Drive/Slack/..." | Claude 会查找并推荐对应的连接器 |
| `suggest_connectors` | 向你推荐未连接的外部应用 | （Claude 主动使用） | 显示"连接"按钮，引导你授权第三方应用 |
| `tool_search` | 加载延迟工具（Gmail、Calendar 等） | "帮我查一下我的日历/邮件" | 先加载工具定义，再调用，否则工具无法使用 |

---

## 三、万能提示词模板

如果你希望 Claude 每次都把所有文件给你，可以在对话开头加上：

```
在这次对话中，请遵守以下规则：
1. 所有脚本和代码必须先用 create_file 保存成文件，不允许用 python3 -c 直接执行
2. 所有生成的文件必须复制到 /mnt/user-data/outputs/
3. 每次回答结束时，用 present_files 把本次生成的所有文件提供给我下载
```

---

## 四、官方参考链接

| 资源 | 链接 |
|---|---|
| Anthropic 官方文档 | https://docs.anthropic.com |
| Claude 使用支持 | https://support.claude.ai |
| Prompt 工程指南 | https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview |
| API 文档 | https://docs.anthropic.com/en/api/getting-started |

> ⚠️ 注意：`create_file`、`present_files`、`bash_tool` 等工具是 Claude.ai 内部实现，Anthropic 没有对外公开这些工具的独立文档页面。以上官方链接是最接近的参考资源。
