---
cssclasses:
  - oup-modern-large
---

←
←
## LaTeX 学习大纲

---

### 第一级：Syntax（让机器看懂你写的东西）

这一级纯靠大量书写内化，不需要深度思考，每天接触一点点。

**1. 基本结构**
- 文档结构 `\documentclass`、`\begin{document}`、`\end{document}`
- 注释 `%`
- 换行与分段

**2. 数学公式**
- 行内公式 `$...$` vs 行间公式 `$$...$$`
- 上下标 `x^2`、`x_i`
- 分数 `\frac{a}{b}`
- 根号 `\sqrt{x}`
- 求和 `\sum`、积分 `\int`
- 希腊字母 `\alpha`、`\beta`、`\pi`
- 常用符号 `\gg`、`\leq`、`\neq`、`\infty`

**3. 文字排版**
- 加粗 `\textbf{}`、斜体 `\textit{}`
- 字体大小
- 对齐方式

**4. 列表与表格**
- 无序列表 `itemize`
- 有序列表 `enumerate`
- 表格 `tabular`

---

### 第二级：表达工具（组织和呈现内容）

这一级开始有逻辑结构，需要稍微深一点的思考。

**5. 文档结构**
- 标题层级 `\section`、`\subsection`、`\subsubsection`
- 目录自动生成 `\tableofcontents`
- 页眉页脚

**6. 图片与浮动体**
- 插入图片 `\includegraphics`
- 图片位置控制 `[h]`、`[t]`、`[b]`
- 图注 `\caption`

**7. 引用与交叉引用**
- 标签 `\label{}`
- 引用 `\ref{}`、`\eqref{}`
- 参考文献 `\cite{}`、BibTeX

**8. 常用宏包**
- `amsmath` — 数学增强
- `graphicx` — 图片
- `geometry` — 页面设置
- `hyperref` — 超链接

---

### 第三级：Algorithms（深度排版与自动化）

这一级需要整块时间沉下心来，像解数学题一样思考。

**9. 自定义命令**
- `\newcommand{}{}` 定义自己的命令
- `\renewcommand{}{}` 重定义已有命令

**10. 复杂数学排版**
- 多行公式对齐 `align`、`cases`
- 矩阵 `matrix`、`bmatrix`、`pmatrix`
- 定理环境 `theorem`、`proof`

**11. 自动化与编程**
- 循环与条件 `\foreach`（TikZ）
- 绘图 TikZ / PGFPlots
- 模板设计

---

### 学习节奏建议

| 级别 | 方式 | 时间投入 |
|------|------|--------|
| 第一级 Syntax | 每天写一点，靠频率内化 | 每天 15 分钟 |
| 第二级 表达工具 | 有需要时查文档，边用边学 | 按需 |
| 第三级 Algorithms | 整块时间，深度攻克 | 每周 1-2 次 |

> 和学 programming 一样：**先具体（直接写公式）→ 视觉化（看渲染结果）→ 再抽象（理解底层逻辑）**。