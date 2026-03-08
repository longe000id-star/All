←
←
# Claude 容器目录结构探索结果

## /mnt 目录结构

```
/mnt
```
- **WHAT**: 容器的挂载根目录
- **DO WHAT**: 所有外部挂载的目录都在这里
- **HOW**: 不需要直接操作，通过子目录访问

```
/mnt/skills
```
- **WHAT**: Claude 技能库的根目录
- **DO WHAT**: 存放所有技能指南（SKILL.md），Claude 执行任务前读取
- **HOW**: 告诉 Claude「先读取对应的 SKILL.md 再开始」

```
/mnt/skills/examples
```
- **WHAT**: 示例技能库目录
- **DO WHAT**: 存放进阶/特定场景的技能，如艺术生成、GIF 制作等
- **HOW**: 描述你的任务，Claude 会自动匹配对应示例技能

```
/mnt/skills/examples/algorithmic-art
```
- **WHAT**: 算法艺术生成技能
- **DO WHAT**: 用 p5.js 生成流场、粒子系统等可交互代码艺术
- **HOW**: 「用代码帮我生成一幅算法艺术」

```
/mnt/skills/examples/algorithmic-art/templates
```
- **WHAT**: 算法艺术的模板文件
- **DO WHAT**: 提供预设的艺术模板供 Claude 参考和复用
- **HOW**: 无需直接操作，Claude 生成艺术时自动引用

```
/mnt/skills/examples/benepass-reimbursement
```
- **WHAT**: Benepass 报销自动化技能
- **DO WHAT**: 自动登录 Benepass 平台、填写表单、上传收据、提交报销
- **HOW**: 「帮我在 Benepass 提交这张收据」（需要浏览器工具）

```
/mnt/skills/examples/brand-guidelines
```
- **WHAT**: Anthropic 品牌视觉规范技能
- **DO WHAT**: 为 Artifact 套用 Anthropic 官方品牌色彩和排版风格
- **HOW**: 「给这个页面套用 Anthropic 的品牌风格」

```
/mnt/skills/examples/canvas-design
```
- **WHAT**: 视觉设计生成技能
- **DO WHAT**: 生成海报、插图、视觉设计，输出为 PNG 或 PDF
- **HOW**: 「帮我设计一张活动海报」

```
/mnt/skills/examples/canvas-design/canvas-fonts
```
- **WHAT**: Canvas 设计用字体库
- **DO WHAT**: 存放设计时可用的字体资源
- **HOW**: 无需直接操作，Claude 设计时自动调用

```
/mnt/skills/examples/doc-coauthoring
```
- **WHAT**: 文档协作写作技能
- **DO WHAT**: 通过结构化迭代流程共同撰写文档、提案、技术规格
- **HOW**: 「我们一起来写一份技术方案」

```
/mnt/skills/examples/internal-comms
```
- **WHAT**: 内部沟通模板技能
- **DO WHAT**: 生成状态报告、领导力更新、事故报告、项目进展等内部文件
- **HOW**: 「帮我写一份项目状态报告」

```
/mnt/skills/examples/internal-comms/examples
```
- **WHAT**: 内部沟通的范例文件
- **DO WHAT**: 提供各类内部沟通的写作范本
- **HOW**: 无需直接操作，Claude 写作时自动参考

```
/mnt/skills/examples/mcp-builder
```
- **WHAT**: MCP 服务器构建技能
- **DO WHAT**: 用 Python (FastMCP) 或 TypeScript 构建 MCP 服务器连接外部 API
- **HOW**: 「帮我写一个连接 Notion API 的 MCP 服务器」

```
/mnt/skills/examples/mcp-builder/reference
```
- **WHAT**: MCP 构建的参考文档
- **DO WHAT**: 存放 MCP 协议规范和 API 参考资料
- **HOW**: 无需直接操作，Claude 构建 MCP 时自动引用

```
/mnt/skills/examples/mcp-builder/scripts
```
- **WHAT**: MCP 构建的辅助脚本
- **DO WHAT**: 提供构建、测试 MCP 服务器的工具脚本
- **HOW**: 无需直接操作，Claude 自动调用

```
/mnt/skills/examples/skill-creator
```
- **WHAT**: 技能创建工具
- **DO WHAT**: 创建新技能、编辑现有技能、测试触发准确性、评估技能性能
- **HOW**: 「帮我创建一个新的技能」

```
/mnt/skills/examples/skill-creator/agents
```
- **WHAT**: 技能创建的 Agent 配置
- **DO WHAT**: 定义用于评估和优化技能的 Agent 行为
- **HOW**: 无需直接操作，skill-creator 工作流自动使用

```
/mnt/skills/examples/skill-creator/assets
```
- **WHAT**: 技能创建的素材文件
- **DO WHAT**: 存放技能创建过程中用到的图片、模板等素材
- **HOW**: 无需直接操作

```
/mnt/skills/examples/skill-creator/eval-viewer
```
- **WHAT**: 技能评估结果查看器
- **DO WHAT**: 可视化展示技能测试的评估结果和性能数据
- **HOW**: 「帮我查看这个技能的评估结果」

```
/mnt/skills/examples/skill-creator/references
```
- **WHAT**: 技能创建的参考资料
- **DO WHAT**: 存放创建高质量技能的规范和最佳实践文档
- **HOW**: 无需直接操作，Claude 创建技能时自动参考

```
/mnt/skills/examples/skill-creator/scripts
```
- **WHAT**: 技能创建的自动化脚本
- **DO WHAT**: 提供批量测试、性能基准测试等自动化工具
- **HOW**: 无需直接操作，skill-creator 工作流自动调用

```
/mnt/skills/examples/slack-gif-creator
```
- **WHAT**: Slack 动态 GIF 生成技能
- **DO WHAT**: 生成符合 Slack 尺寸和文件大小限制的动态 GIF
- **HOW**: 「帮我做一个可以发 Slack 的动态 GIF」

```
/mnt/skills/examples/slack-gif-creator/core
```
- **WHAT**: GIF 生成的核心工具库
- **DO WHAT**: 存放 GIF 生成、压缩、验证的核心脚本
- **HOW**: 无需直接操作，Claude 生成 GIF 时自动调用

```
/mnt/skills/examples/theme-factory
```
- **WHAT**: Artifact 主题样式工具
- **DO WHAT**: 为幻灯片、文档、HTML 页面套用 10 种预设主题或自定义主题
- **HOW**: 「给这个 artifact 套一个深色主题」

```
/mnt/skills/examples/theme-factory/themes
```
- **WHAT**: 预设主题文件库
- **DO WHAT**: 存放 10 种预设主题的颜色、字体、样式配置
- **HOW**: 无需直接操作，Claude 套用主题时自动读取

```
/mnt/skills/examples/web-artifacts-builder
```
- **WHAT**: 复杂 Web Artifact 构建套件
- **DO WHAT**: 用 React + Tailwind + shadcn/ui 构建多页面、多组件的复杂 Web 应用
- **HOW**: 「帮我做一个带导航栏和多个 Tab 的 Dashboard」

```
/mnt/skills/examples/web-artifacts-builder/scripts
```
- **WHAT**: Web Artifact 构建的辅助脚本
- **DO WHAT**: 提供组件生成、代码验证等工具脚本
- **HOW**: 无需直接操作，Claude 构建时自动调用

```
/mnt/skills/public
```
- **WHAT**: 公开技能库根目录
- **DO WHAT**: 存放所有人都能使用的核心技能（Word、PDF、PPT、Excel 等）
- **HOW**: 描述文件类型需求，Claude 自动读取对应技能

```
/mnt/skills/public/docx
```
- **WHAT**: Word 文档生成技能
- **DO WHAT**: 创建、读取、编辑专业 Word 文档，含目录、标题、页码、表格
- **HOW**: 「帮我写一份报告，保存为 Word 文件」

```
/mnt/skills/public/docx/scripts
```
- **WHAT**: docx 生成的核心脚本库
- **DO WHAT**: 存放生成 .docx 文件的 Python/JS 脚本工具
- **HOW**: 无需直接操作，Claude 生成 Word 文件时自动调用

```
/mnt/skills/public/docx/scripts/office
```
- **WHAT**: Office XML 处理工具集
- **DO WHAT**: 处理 Word 文档底层 XML 结构
- **HOW**: 无需直接操作

```
/mnt/skills/public/docx/scripts/office/helpers
```
- **WHAT**: Office 处理辅助函数库
- **DO WHAT**: 提供格式转换、样式处理等常用辅助函数
- **HOW**: 无需直接操作

```
/mnt/skills/public/docx/scripts/office/schemas
```
- **WHAT**: Office 文档格式 Schema 定义根目录
- **DO WHAT**: 存放验证 Word 文档格式合规性的所有 XML Schema
- **HOW**: 无需直接操作，Claude 生成文档时自动验证

```
/mnt/skills/public/docx/scripts/office/schemas/ISO-IEC29500-4_2016
```
- **WHAT**: ISO/IEC 29500-4:2016 国际标准 Schema
- **DO WHAT**: 确保生成的 Word 文件符合国际标准，跨平台兼容
- **HOW**: 无需直接操作

```
/mnt/skills/public/docx/scripts/office/schemas/ecma
```
- **WHAT**: ECMA-376 标准 Schema 根目录
- **DO WHAT**: Office Open XML 的 ECMA 国际标准定义
- **HOW**: 无需直接操作

```
/mnt/skills/public/docx/scripts/office/schemas/ecma/fouth-edition
```
- **WHAT**: ECMA-376 第四版 Schema
- **DO WHAT**: 对应 Office 2016+ 格式的规范定义
- **HOW**: 无需直接操作

```
/mnt/skills/public/docx/scripts/office/schemas/mce
```
- **WHAT**: MCE 标记兼容性扩展 Schema
- **DO WHAT**: 处理 Office 文档向前/向后兼容性
- **HOW**: 无需直接操作

```
/mnt/skills/public/docx/scripts/office/schemas/microsoft
```
- **WHAT**: Microsoft 专有扩展 Schema
- **DO WHAT**: 处理微软私有的 Office XML 扩展功能
- **HOW**: 无需直接操作

```
/mnt/skills/public/docx/scripts/office/validators
```
- **WHAT**: 文档格式验证器
- **DO WHAT**: 验证生成的 Word 文档是否符合规范，确保能正常打开
- **HOW**: 无需直接操作，Claude 生成文档后自动验证

```
/mnt/skills/public/docx/scripts/templates
```
- **WHAT**: Word 文档模板库
- **DO WHAT**: 提供报告、信件、备忘录等预设 Word 模板
- **HOW**: 「用模板帮我生成一份正式报告」

```
/mnt/skills/public/frontend-design
```
- **WHAT**: 前端 UI 设计技能
- **DO WHAT**: 生成美观、专业级的网页、React 组件、Dashboard、Landing Page
- **HOW**: 「帮我做一个产品落地页，要好看」

```
/mnt/skills/public/pdf
```
- **WHAT**: PDF 处理技能
- **DO WHAT**: 创建、合并、拆分 PDF，提取文字，加水印，OCR 扫描件
- **HOW**: 「把这几个 PDF 合并成一个」

```
/mnt/skills/public/pdf/scripts
```
- **WHAT**: PDF 处理脚本库
- **DO WHAT**: 存放 PDF 生成和处理的 Python 脚本工具
- **HOW**: 无需直接操作，Claude 处理 PDF 时自动调用

```
/mnt/skills/public/pptx
```
- **WHAT**: PowerPoint 生成技能
- **DO WHAT**: 创建演示文稿、修改现有 PPT、处理幻灯片布局和样式
- **HOW**: 「帮我做一个关于 AI 趋势的 PPT」

```
/mnt/skills/public/pptx/scripts
```
- **WHAT**: pptx 生成的核心脚本库
- **DO WHAT**: 存放生成 .pptx 文件的工具脚本
- **HOW**: 无需直接操作，Claude 生成 PPT 时自动调用

```
/mnt/skills/public/pptx/scripts/office
```
- **WHAT**: pptx Office XML 处理工具集
- **DO WHAT**: 处理 PPT 文档底层 XML 结构
- **HOW**: 无需直接操作

```
/mnt/skills/public/pptx/scripts/office/helpers
```
- **WHAT**: pptx Office 处理辅助函数库
- **DO WHAT**: 提供 PPT 格式转换、样式处理等常用辅助函数
- **HOW**: 无需直接操作

```
/mnt/skills/public/pptx/scripts/office/schemas
```
- **WHAT**: pptx Office 文档格式 Schema 定义根目录
- **DO WHAT**: 存放验证 PPT 文档格式合规性的所有 XML Schema
- **HOW**: 无需直接操作，Claude 生成 PPT 时自动验证

```
/mnt/skills/public/pptx/scripts/office/schemas/ISO-IEC29500-4_2016
```
- **WHAT**: pptx ISO/IEC 29500-4:2016 国际标准 Schema
- **DO WHAT**: 确保生成的 PPT 文件符合国际标准，跨平台兼容
- **HOW**: 无需直接操作

```
/mnt/skills/public/pptx/scripts/office/schemas/ecma
```
- **WHAT**: pptx ECMA-376 标准 Schema 根目录
- **DO WHAT**: PPT 的 Office Open XML ECMA 国际标准定义
- **HOW**: 无需直接操作

```
/mnt/skills/public/pptx/scripts/office/schemas/ecma/fouth-edition
```
- **WHAT**: pptx ECMA-376 第四版 Schema
- **DO WHAT**: 对应 PowerPoint 2016+ 格式的规范定义
- **HOW**: 无需直接操作

```
/mnt/skills/public/pptx/scripts/office/schemas/mce
```
- **WHAT**: pptx MCE 标记兼容性扩展 Schema
- **DO WHAT**: 处理 PPT 文档向前/向后兼容性
- **HOW**: 无需直接操作

```
/mnt/skills/public/pptx/scripts/office/schemas/microsoft
```
- **WHAT**: pptx Microsoft 专有扩展 Schema
- **DO WHAT**: 处理微软私有的 PPT XML 扩展功能
- **HOW**: 无需直接操作

```
/mnt/skills/public/pptx/scripts/office/validators
```
- **WHAT**: pptx 文档格式验证器
- **DO WHAT**: 验证生成的 PPT 是否符合规范，确保能正常打开
- **HOW**: 无需直接操作，Claude 生成 PPT 后自动验证

```
/mnt/skills/public/product-self-knowledge
```
- **WHAT**: Anthropic 产品知识库
- **DO WHAT**: 确保 Claude 回答 API、定价、模型、功能等问题时信息准确不过时
- **HOW**: 「Claude API 的 rate limit 是多少？」

```
/mnt/skills/public/xlsx
```
- **WHAT**: Excel 处理技能
- **DO WHAT**: 创建表格、计算公式、清洗数据、绘制图表，支持 .xlsx/.csv/.tsv
- **HOW**: 「把这份 CSV 数据整理成 Excel 表格」

```
/mnt/skills/public/xlsx/scripts
```
- **WHAT**: xlsx 生成的核心脚本库
- **DO WHAT**: 存放生成 .xlsx 文件的工具脚本
- **HOW**: 无需直接操作，Claude 生成 Excel 时自动调用

```
/mnt/skills/public/xlsx/scripts/office
```
- **WHAT**: xlsx Office XML 处理工具集
- **DO WHAT**: 处理 Excel 文档底层 XML 结构
- **HOW**: 无需直接操作

```
/mnt/skills/public/xlsx/scripts/office/helpers
```
- **WHAT**: xlsx Office 处理辅助函数库
- **DO WHAT**: 提供 Excel 格式转换、样式处理等常用辅助函数
- **HOW**: 无需直接操作

```
/mnt/skills/public/xlsx/scripts/office/schemas
```
- **WHAT**: xlsx Office 文档格式 Schema 定义根目录
- **DO WHAT**: 存放验证 Excel 文档格式合规性的所有 XML Schema
- **HOW**: 无需直接操作，Claude 生成 Excel 时自动验证

```
/mnt/skills/public/xlsx/scripts/office/schemas/ISO-IEC29500-4_2016
```
- **WHAT**: xlsx ISO/IEC 29500-4:2016 国际标准 Schema
- **DO WHAT**: 确保生成的 Excel 文件符合国际标准，跨平台兼容
- **HOW**: 无需直接操作

```
/mnt/skills/public/xlsx/scripts/office/schemas/ecma
```
- **WHAT**: xlsx ECMA-376 标准 Schema 根目录
- **DO WHAT**: Excel 的 Office Open XML ECMA 国际标准定义
- **HOW**: 无需直接操作

```
/mnt/skills/public/xlsx/scripts/office/schemas/ecma/fouth-edition
```
- **WHAT**: xlsx ECMA-376 第四版 Schema
- **DO WHAT**: 对应 Excel 2016+ 格式的规范定义
- **HOW**: 无需直接操作

```
/mnt/skills/public/xlsx/scripts/office/schemas/mce
```
- **WHAT**: xlsx MCE 标记兼容性扩展 Schema
- **DO WHAT**: 处理 Excel 文档向前/向后兼容性
- **HOW**: 无需直接操作

```
/mnt/skills/public/xlsx/scripts/office/schemas/microsoft
```
- **WHAT**: xlsx Microsoft 专有扩展 Schema
- **DO WHAT**: 处理微软私有的 Excel XML 扩展功能
- **HOW**: 无需直接操作

```
/mnt/skills/public/xlsx/scripts/office/validators
```
- **WHAT**: xlsx 文档格式验证器
- **DO WHAT**: 验证生成的 Excel 是否符合规范，确保能正常打开
- **HOW**: 无需直接操作，Claude 生成 Excel 后自动验证

```
/mnt/transcripts
```
- **WHAT**: 对话记录存储目录
- **DO WHAT**: 存储历史对话记录供 Claude 参考上下文
- **HOW**: 无需直接操作，系统自动管理

```
/mnt/user-data
```
- **WHAT**: 用户数据根目录
- **DO WHAT**: 存放所有与当前用户相关的文件（上传、输出、工具结果）
- **HOW**: 通过子目录 uploads/ 和 outputs/ 与 Claude 交换文件

```
/mnt/user-data/tool_results
```
- **WHAT**: 工具调用的中间结果缓存
- **DO WHAT**: 临时存放工具执行产生的中间数据
- **HOW**: 无需直接操作，系统自动管理

```
/mnt/user-data/outputs
```
- **WHAT**: Claude 输出文件目录
- **DO WHAT**: Claude 把生成的文件放这里，你才能通过 present_files 下载
- **HOW**: 「把所有输出文件保存到 outputs 并给我下载链接」

```
/mnt/user-data/uploads
```
- **WHAT**: 用户上传文件目录
- **DO WHAT**: 你在对话中上传的所有文件自动出现在这里，Claude 可读取处理
- **HOW**: 直接在对话中上传文件，然后说「处理我上传的文件」


---

## /home/claude/ 内容

```
. (/home/claude/)
```
- **WHAT**: Claude 的临时工作区根目录
- **DO WHAT**: Claude 在这里创建、编译、测试中间文件
- **HOW**: 要求 Claude 把最终文件移到 outputs/，否则你看不到

```
.. (/)
```
- **WHAT**: 容器根目录
- **DO WHAT**: 系统根目录，包含所有挂载点
- **HOW**: 无需直接操作

```
.cache
```
- **WHAT**: 应用缓存目录
- **DO WHAT**: 存放 pip、npm 等工具的下载缓存，加速重复安装
- **HOW**: 无需直接操作，安装包时自动使用

```
.config
```
- **WHAT**: 应用配置目录
- **DO WHAT**: 存放各种工具的配置文件
- **HOW**: 无需直接操作

```
.local
```
- **WHAT**: 用户本地数据目录
- **DO WHAT**: 存放用户级安装的软件和数据
- **HOW**: 无需直接操作

```
.npm
```
- **WHAT**: npm 配置和缓存目录
- **DO WHAT**: 存放 npm 的缓存数据，加速 Node 包安装
- **HOW**: 无需直接操作，npm install 时自动使用

```
.npm-global
```
- **WHAT**: npm 全局包安装目录
- **DO WHAT**: 全局安装的 Node.js 工具包都在这里
- **HOW**: 「用 npm 安装 X 工具」时 Claude 自动安装到这里

```
.npmrc
```
- **WHAT**: npm 配置文件
- **DO WHAT**: 定义 npm 的全局配置（如全局安装路径、registry 等）
- **HOW**: 无需直接操作

```
.wget-hsts
```
- **WHAT**: wget 的 HSTS 缓存文件
- **DO WHAT**: 记录支持 HTTPS 强制跳转的域名，提升下载安全性
- **HOW**: 无需直接操作

```
test_code.py
```
- **WHAT**: 本次对话生成的测试脚本
- **DO WHAT**: 之前用来测试你的 Python bisection 代码的被测文件
- **HOW**: 对话结束后自动清空，正式文件应放在 outputs/
