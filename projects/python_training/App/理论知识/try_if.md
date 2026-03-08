←
←
# Python 笔记：`if` vs `try` 判断 float 合法性

---

## 背景问题

在验证用户输入的 `yearly_salary` 是否是合法数字时，我想到了两种方式：

**我的问题：** 为什么不能直接用 `if float(yearly_salary)` 来判断？能转化就返回 True，不能转换就返回 False？

---

## 方法一：`if float()` ❌ 有坑

```python
if float(yearly_salary):
    print("合法")
else:
    print("不合法")
```

### 问题 1：`float()` 不返回 True/False

`float()` 返回的是**转换后的数字**，不是布尔值：

```python
float("3.14")  # 返回 3.14，不是 True
float("0")     # 返回 0.0，不是 True
```

### 问题 2：`"0"` 会被误判为不合法

```python
if float("0"):   # 0.0 → Python 判定为 False
    print("合法") # ❌ 不会执行，但 "0" 明明是合法数字！
```

**原因：** 在 Python 里，`0.0` 被视为 `False`。

### 问题 3：非法字符串直接崩溃

```python
float("abc")  # 💥 抛出 ValueError，程序崩溃
              # 根本到不了 else
```

`if/else` 处理不了"转换失败"的情况，因为程序在转换时就已经崩溃了。

### 总结对比表

| 输入 | `float()` 返回 | `if` 判断结果 | 正确吗？ |
|------|--------------|-------------|--------|
| `"3.14"` | `3.14` | True | ✅ |
| `"0"` | `0.0` | **False** | ❌ 误判 |
| `"abc"` | 报错崩溃 | 到不了 if | ❌ 崩溃 |

---

## 方法二：`try/except` ✅ 正确做法

```python
def is_valid_salary(yearly_salary):
    try:
        float(yearly_salary)
        return True
    except ValueError:
        return False
```

### 为什么 try 可以？

**我的疑问：** 那么为什么 `try` 可以？

**答：** 因为 `try` 判断的是**"有没有报错"**，而不是"返回值是什么"：

```python
# if 判断的是：返回值是 True 还是 False
if float("0"):   # 看 0.0 → False ❌

# try 判断的是：有没有崩溃报错
try:
    float("0")   # 能运行，没报错 → 走 return True ✅
except ValueError:
    return False
```

`try` 完全绕开了返回值是 `0.0` 还是 `3.14` 的问题，只关心 **"这行代码能不能顺利跑完"**。

### 测试结果

```python
is_valid_salary("3.14")    # True  ✅
is_valid_salary("50000")   # True  ✅
is_valid_salary("0")       # True  ✅ 不会误判！
is_valid_salary("abc")     # False ✅ 不会崩溃！
is_valid_salary("")        # False ✅
```

---

## 核心结论

| | 判断的是 | 能处理报错？ | `"0"` 会误判？ |
|--|--------|-----------|-------------|
| `if` | 返回值的真假 | ❌ | ❌ |
| `try` | 执行过程有没有报错 | ✅ | ✅ |

> **一句话：** `if` 看结果，`try` 看过程。
> 只要可能报错，就用 `try`，不要用 `if`。

---

## 补充：字符串输入完全没问题

`float()` 天生就能处理字符串，不需要先转换：

```python
float("3.14")   # → 3.14  ✅
float("99")     # → 99.0  ✅
float("abc")    # → 报 ValueError，被 except 捕获 ✅
float("")       # → 报 ValueError，被 except 捕获 ✅
```