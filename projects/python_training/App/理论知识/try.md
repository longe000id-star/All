---
cssclasses:
  - oup-modern-large
---

←
←
## `try/except` 通用格式

```python
try:
    <可能出错的代码>
except <错误类型>:
    <出错时执行>
```

---

## 所有相关语句

### 1. 基本 `try/except`
```python
try:
    float("abc")
except ValueError:
    print("转换失败")
```

### 2. 捕获多种错误
```python
try:
    x = int(input())
    print(10 / x)
except ValueError:
    print("不是数字")
except ZeroDivisionError:
    print("不能除以0")
```

### 3. `else` — 没有报错时执行
```python
try:
    x = float("3.14")
except ValueError:
    print("失败")
else:
    print("成功，值是", x)  # 只有没报错才执行
```

### 4. `finally` — 无论如何都执行
```python
try:
    x = float("abc")
except ValueError:
    print("失败")
finally:
    print("无论成功失败，我都执行")  # 常用于关闭文件/数据库
```

### 5. 完整结构（四者合用）
```python
try:
    x = float("3.14")
except ValueError:
    print("出错了")
else:
    print("成功")
finally:
    print("结束")
```

### 6. 捕获所有错误（`Exception`）
```python
try:
    x = 10 / 0
except Exception as e:
    print("错误是：", e)  # 错误是：division by zero
```

### 7. 主动抛出错误（`raise`）
```python
def check_salary(salary):
    if salary < 0:
        raise ValueError("工资不能为负数")

try:
    check_salary(-100)
except ValueError as e:
    print(e)  # 工资不能为负数
```

---

## 结构总结

```python
try:
    ...
except 错误类型:      # 必须有，可以多个
    ...
else:                # 可选，没报错时执行
    ...
finally:             # 可选，无论如何都执行
    ...
```

| 关键词 | 作用 | 是否必须 |
|--------|------|--------|
| `try` | 包裹可能出错的代码 | ✅ |
| `except` | 捕获错误并处理 | ✅ |
| `else` | 无错误时执行 | 可选 |
| `finally` | 无论如何都执行 | 可选 |
| `raise` | 主动抛出错误 | 可选 |