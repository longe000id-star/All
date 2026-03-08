←
←
# Python 笔记：`while` 循环

---

## 一、通用结构

```python
while 条件:
    循环体
```

就这么简单，不需要可迭代对象，只需要一个**能判断 True/False 的条件**。

---

## 二、关键词

| 关键词 | 作用 | 是否必须 |
|--------|------|--------|
| `while` | 启动循环，判断条件 | ✅ |
| `break` | 立即终止整个循环 | 可选 |
| `continue` | 跳过本次，进入下一次 | 可选 |
| `else` | 循环正常结束（没被 break）时执行 | 可选 |

---

## 三、所有使用类型

### 1. 基本条件循环
**什么时候用：** 知道终止条件，但不知道要循环几次。

```python
x = 0
while x < 5:
    print(x)
    x += 1   # 必须让条件趋向 False，否则死循环
# 输出：0 1 2 3 4
```

---

### 2. `while True` + `break` — 无限循环手动退出
**什么时候用：** 不知道什么时候停，直到满足某个条件才退出。

```python
while True:
    x = int(input("输入一个正数: "))
    if x > 0:
        break   # 满足条件才退出
print("输入正确:", x)
```

---

### 3. 用户输入验证
**什么时候用：** 用户可能一直输错，要不断重问直到输对。

```python
while True:
    try:
        salary = float(input("输入工资: "))
        break   # 输入合法才跳出
    except ValueError:
        print("无效，请重试")
```

---

### 4. 条件范围验证
**什么时候用：** 输入的值必须在某个范围内，否则一直重问。

```python
while portion_saved > 1:
    portion_saved = float(input("请输入 0~1 之间的数: "))
```

---

### 5. 计数器循环
**什么时候用：** 需要手动控制计数，比 `for` 更灵活。

```python
count = 0
while count < 3:
    print("第", count+1, "次")
    count += 1
```

---

### 6. `while...else`
**什么时候用：** 循环正常结束（没被 `break` 打断）后需要执行某段代码。

```python
x = 0
while x < 3:
    x += 1
else:
    print("正常结束")   # 没有 break，所以会执行
```

---

### 7. `continue` — 跳过某次循环
**什么时候用：** 某些情况下不想执行循环体，直接进入下一次。

```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue   # 跳过 x==3 这次
    print(x)
# 输出：1 2 4 5
```

---

## 四、`for` vs `while` 一句话

| | 依赖 | 适合场景 |
|--|------|--------|
| `for` | 可迭代对象 | 知道循环几次，或遍历集合 |
| `while` | 条件 | 不知道循环几次，直到条件满足 |

---

## 五、最重要的注意点

> `while` 循环必须确保条件最终会变为 `False`，否则**死循环**，程序永远不会停。
>
> 唯一例外是 `while True`，但此时必须有 `break` 来手动退出。

是的！Python 的 `while` 循环条件可以使用 `and`、`or`、`not` 逻辑运算符。

**`and` — 两个条件都为真才继续循环**
```python
x = 0
y = 10
while x < 5 and y > 0:
    x += 1
    y -= 2
# x=5 时停止（第一个条件为假）
```

**`or` — 任一条件为真就继续循环**
```python
x = 0
y = 10
while x < 3 or y > 5:
    x += 1
    y -= 1
# 两个条件都为假才停止
```

**`not` — 取反条件**
```python
done = False
while not done:
    # 做一些事情
    done = True  # 改变条件，退出循环
```

**组合使用**
```python
x = 0
flag = True
while flag and not x >= 5:
    x += 1
    if x == 3:
        flag = False
# flag 变为 False 时停止
```

总结一下：

| 运算符 | 含义 | 用法 |
|--------|------|------|
| `and` | 且 | 所有条件为真才循环 |
| `or` | 或 | 任一条件为真就循环 |
| `not` | 非 | 条件取反 |

和 `if` 语句一样，`while` 的条件本质上就是一个布尔表达式，所以逻辑运算符完全适用。