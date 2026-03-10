---
cssclasses:
  - oup-modern-large
---

←
←
# 二分搜索（Bisection Search）权威资源合集

生成日期：2026年3月8日

---

## 🎓 MIT OpenCourseWare（最推荐）

### MIT 6.100L — Lecture 6: Bisection Search
**主讲：Dr. Ana Bell ｜ Fall 2022**

- 📄 课件 PDF：[mit6_100l_f22_lec06.pdf](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_lec06.pdf)
- 🎬 视频讲座：[Lecture 6 Video](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/resources/6100l-lecture-6-multi-version-3_mp4/)
- 📚 全课程材料：[Material by Lecture](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/material-by-lecture/)
- 📦 全套视频下载（Internet Archive）：[archive.org/details/mit6_100lf22](https://archive.org/details/mit6_100lf22)

### MIT 6.0001 — Lecture 3: Bisection Search（经典旧版）
**主讲：Dr. Ana Bell ｜ Fall 2016**

- 🎬 视频讲座：[Lecture 3 - Bisection](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-3-string-manipulation-guess-and-check-approximations-bisection/)

---

## 🌲 Stanford University

### Stanford Math 114 — Bisection Method Notes
**数学系数值分析课讲义，含收敛性证明与误差分析**

- 📄 讲义 PDF：[bisection_method_notes.pdf](https://web.stanford.edu/class/math114/lecture_notes/bisection_method_notes.pdf)

### Stanford CS161 — Algorithms（含 Binary Search）
**算法与数据结构课，2025-2026学年**

- 🌐 课程主页：[cs161-stanford.github.io](https://cs161-stanford.github.io/)

---

## 📖 权威教学网站

### Mathematics LibreTexts — Bisection Method
开源大学数学教材，含算法步骤、例题、误差分析

- 🌐 [Bisection Methods for Solving a Nonlinear Equation](https://math.libretexts.org/Workbench/Numerical_Methods_with_Applications_(Kaw)/3:_Nonlinear_Equations/3.03:_Bisection_Methods_for_Solving_a_Nonlinear_Equation)

### GeeksforGeeks — Bisection Method
含 Python / C++ / Java 多语言代码，2025年更新

- 🌐 [program-for-bisection-method](https://www.geeksforgeeks.org/dsa/program-for-bisection-method/)

### Wikipedia
- 🌐 二分法：[Bisection Method](https://en.wikipedia.org/wiki/Bisection_method)
- 🌐 二分搜索算法：[Binary Search](https://en.wikipedia.org/wiki/Binary_search)

---

## 💻 核心代码模板

```python
# 标准二分搜索模板（适用于本题）
r_min, r_max = 0.0, 1.0
epsilon = 1e-7

while True:
    r_mid = (r_min + r_max) / 2
    amount = initial * (1 + r_mid/12) ** 36

    if abs(amount - target) < 100:  # 找到答案
        r = r_mid
        break
    elif amount < target:           # 太小，增大 r
        r_min = r_mid
    else:                           # 太大，减小 r
        r_max = r_mid

    if r_max - r_min < epsilon:     # 无解
        r = None
        break
```

```python
# Python 内置 bisect 模块（用于有序列表）
import bisect

a = [1, 3, 5, 7, 9]
bisect.insort(a, 4)              # 插入并保持有序: [1,3,4,5,7,9]
pos = bisect.bisect_left(a, 5)  # 找到5的位置: 3
```

---

## 📐 关键公式

| 公式 | 说明 |
|------|------|
| `最多迭代次数 = log2((b-a) / epsilon)` | 给定误差范围所需的最大循环次数 |
| `abs(amount_saved - target) < 100` | 判断是否在可接受范围内（exclusive） |
| `amount = P × (1 + r/12)^36` | 本题的复利计算公式 |
