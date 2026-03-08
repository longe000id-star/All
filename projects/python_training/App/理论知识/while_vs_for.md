←
←
# Python 笔记：`for` vs `while` 循环

"所以这里 while 是不需要可迭代对象，而 if 需要？"
这是 `for` 和 `while` 最本质的区别：

---

## `for` — 必须有可迭代对象

```python
for i in [1, 2, 3]:   # 必须有 "in 某个东西"
```

`for` 是从**集合里逐个取元素**，没有集合就没法用。

---

## `while` — 只需要一个条件

```python
while 条件:   # 只判断 True/False，不需要集合
```

`while` 只关心**条件是否成立**，跟有没有集合完全无关。

---

## 一句话

> `for` 依赖**数据**（从哪里取），`while` 依赖**条件**（什么时候停）。

所以当你不知道要循环几次、没有固定集合可以遍历时，就用 `while`。

---

## 一、基本结构对比

### `for` 循环
```python
for 变量 in 可迭代对象:
    循环体
```
- 适合：**知道循环次数**，或遍历一个集合
- 自动取出每个元素，不需要手动管理索引

### `while` 循环
```python
while 条件:
    循环体
```
- 适合：**不知道循环次数**，直到某个条件满足才停止
- 需要自己确保条件最终会变为 `False`，否则死循环

---

## 二、什么时候用 `for`，什么时候用 `while`

| 场景 | 用哪个 |
|------|--------|
| 遍历列表、字符串、字典 | `for` |
| 循环固定次数（如 10 次） | `for` + `range()` |
| 不知道要循环几次，直到条件满足 | `while` |
| 用户输入验证，直到输对为止 | `while True` + `break` |
| 无限循环 | `while True` |

---

## 三、`range()` 不支持无穷大

**我的问题：** 可以 `for i in range(无限)` 吗？

不可以，`range()` 只接受整数，不支持 `float('inf')`：

```python
for i in range(float('inf'))  # 💥 TypeError: 'float' object cannot be interpreted as an integer
```

**无限循环必须用 `while True`：**

```python
while True:
    # 做某件事
    if 条件满足:
        break  # 满足条件才退出
```

---

## 四、`for...else` 的正确理解

`for` 循环有一个可选的 `else`，**只在循环正常结束（没有被 `break` 打断）时执行**。

```python
for i in range(5):
    if i == 3:
        break
else:
    print("正常结束才执行")  # 被 break 打断，不会执行
```

### ❌ 我的错误用法

```python
for i in range(len(data)):
    try:
        float(data[i])
    except ValueError:
        data[i] = input(f"{text[i]}: ")
else:
    yearly_salary = abs(float(yearly_salary))  # ❌ 用的还是原始变量！
```

**问题：** `else` 里转换的是 `yearly_salary` 原始变量，而不是 `data[0]`，验证后的结果完全没有被用上。

### ✅ 正确写法

```python
for i in range(len(data)):
    try:
        data[i] = float(data[i])  # 直接把转换结果存回 data
    except ValueError:
        data[i] = input(f"{text[i]}: ")

# 循环结束后再统一赋值
yearly_salary      = abs(data[0])
portion_saved      = abs(data[1])
cost_of_dream_home = abs(data[2])
```

---

## 五、用户输入验证：只问一次 vs 不断循环

### ❌ 错误：用户输错后只重问一次

```python
for i in range(len(data)):
    try:
        data[i] = float(data[i])
    except ValueError:
        data[i] = input(f"无效输入，请重新输入 {text[i]}: ")  # 用户再次输错怎么办？
```

用户第二次还是可能输错，`except` 只执行一次，第二次错误就没有处理了。

### ✅ 正确：用 `while True` 不断循环直到输对

```python
for i in range(len(data)):
    while True:
        try:
            data[i] = float(data[i])
            break  # 成功才跳出 while
        except ValueError:
            data[i] = input(f"无效输入，请重新输入 {text[i]}: ")
```

**原理：** `while True` 一直循环，只有 `float()` 成功转换后才 `break` 跳出，否则一直重问。

### 同样的问题：范围验证只检查一次

```python
# ❌ 错误：用户还是可能再次输入 > 1
if portion_saved > 1:
    portion_saved = float(input("The portion should not bigger than 1: "))

# ✅ 正确：while 一直检查直到合法
while portion_saved > 1:
    portion_saved = float(input("The portion should not bigger than 1: "))
```

---

## 六、`while True` 处理用户输入的标准模式

```python
while True:
    try:
        yearly_salary = float(input("Your yearly salary: "))
        break  # 输入合法才跳出循环
    except ValueError:
        print("无效输入，请重试")
```

这是 Python 中处理用户输入验证的**最标准写法**。

---

## 七、`and` / `or` 优先级陷阱

**我的错误：**

```python
if yearly_salary == 0 or portion_saved == 0 and cost_of_dream_home != 0:
```

Python 里 `and` 优先级高于 `or`，实际执行顺序是：

```python
if yearly_salary == 0 or (portion_saved == 0 and cost_of_dream_home != 0):  # ❌ 不是想要的
```

**正确写法，加括号明确优先级：**

```python
if (yearly_salary == 0 or portion_saved == 0) and cost_of_dream_home != 0:  # ✅
```

> **规则：** `and` > `or`，有歧义时永远加括号。

---

## 八、无穷大后继续计算的问题

**我的错误：**

```python
if yearly_salary == 0 or portion_saved == 0:
    months = float('inf')
    print("Number of months:", months)

# 💥 下面还是继续执行了！
monthly_saving = (yearly_salary / 12) * portion_saved  # 除以 0 崩溃
months = math.log(...) / math.log(1 + r) + 1
```

**正确写法，用 `if/else` 互斥：**

```python
if (yearly_salary == 0 or portion_saved == 0) and cost_of_dream_home != 0:
    print("Number of months: inf")
else:
    monthly_saving = (yearly_salary / 12) * portion_saved
    target = cost_of_dream_home * portion_down_payment
    months = math.log(target / monthly_saving) / math.log(1 + r) + 1
    print("Number of months:", months)
```

---

## 九、本次代码问题总结

| 问题 | 严重程度 | 解决方案 |
|------|--------|--------|
| `for...else` 没用上 `data[]` 的结果 | ❌ 严重 | 直接存回 `data[i]` |
| 输错只问一次 | ❌ 严重 | 用 `while True` + `break` |
| `portion_saved > 1` 只检查一次 | ⚠️ 中 | 改 `if` 为 `while` |
| `and/or` 优先级错误 | ⚠️ 中 | 加括号明确优先级 |
| 无穷大后继续计算 | ❌ 严重 | 用 `if/else` 互斥 |

---

## 十、一句话总结

> - **`for`** — 知道循环多少次，或遍历集合用它
> - **`while`** — 不知道循环几次，直到条件满足用它
> - **`while True` + `break`** — 无限循环 + 手动控制退出，是用户输入验证的标准模式