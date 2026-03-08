←
←
## `for` 语句的通用结构

```python
for 变量 in 可迭代对象:
    循环体
else:          # 可选
    收尾代码
```

---

## 关键词只有两个

| 关键词 | 作用 |
|--------|------|
| `for` | 开始循环 |
| `in` | 指定迭代来源 |

---

## 配合使用的关键词（不属于for本身）

| 关键词 | 作用 |
|--------|------|
| `break` | 立即终止整个循环 |
| `continue` | 跳过本次，进入下一次 |
| `else` | 循环**正常结束**后执行（被break打断则不执行） |

---

## 一句话总结

> `for` 的本质就是：**依次从"某个东西"里取出每一项，赋值给变量，执行一次循环体。**

`in` 后面能放什么，决定了 `for` 能做什么。



## Python 中所有 `for` 语句类型

### 1. 基本 for 循环
```python
for i in [1, 2, 3]:
    print(i)
```

### 2. 遍历字符串
```python
for char in "hello":
    print(char)
```

### 3. range() 循环
```python
for i in range(10):        # 0-9
for i in range(2, 10):     # 2-9
for i in range(0, 10, 2):  # 步长为2
```

### 4. 遍历字典
```python
for key in d:                    # 遍历键
for key in d.keys():             # 遍历键
for val in d.values():           # 遍历值
for key, val in d.items():       # 遍历键值对
```

### 5. enumerate() — 带索引遍历
```python
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)  # 0 a, 1 b, 2 c
```

### 6. zip() — 并行遍历多个序列
```python
for a, b in zip([1, 2], ['x', 'y']):
    print(a, b)
```

### 7. 解包遍历（元组/列表）
```python
pairs = [(1, 'a'), (2, 'b')]
for num, letter in pairs:
    print(num, letter)
```

### 8. 嵌套 for 循环
```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

### 9. 列表推导式中的 for
```python
squares = [x**2 for x in range(10)]
filtered = [x for x in range(10) if x % 2 == 0]
```

### 10. 字典 / 集合推导式中的 for
```python
d = {k: v for k, v in pairs}
s = {x**2 for x in range(5)}
```

### 11. 生成器表达式中的 for
```python
gen = (x**2 for x in range(10))
```

### 12. for...else
```python
for i in range(5):
    if i == 3:
        break
else:
    print("未被 break 中断时执行")
```

### 13. 带 continue / break 的 for
```python
for i in range(10):
    if i == 5: break     # 提前终止
    if i % 2: continue   # 跳过本次迭代
```

### 14. 遍历文件行
```python
for line in open("file.txt"):
    print(line)
```

### 15. 遍历自定义迭代器
```python
class MyIter:
    def __iter__(self): return self
    def __next__(self): ...

for item in MyIter():
    print(item)
```

---

**核心规律**：Python 的 `for` 本质上是对任何**可迭代对象**（实现了 `__iter__` 的对象）的遍历，以上所有类型都是这一机制的不同应用场景。

