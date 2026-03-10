---
cssclasses:
  - oup-modern-large
---

←
←
## 一、Python 所有数据类型

- **int**（整数）→ 没有小数点的数字，比如 `1`, `42`, `-7`
  - 使用场景：计数、索引、循环次数
  - 例子：`age = 25`

- **float**（浮点数）→ 有小数点的数字，比如 `3.14`, `-0.5`
  - 使用场景：需要精度的数字，比如价格、温度、坐标
  - 例子：`price = 9.99`

- **complex**（复数）→ 数学里的复数，比如 `3+5j`
  - 使用场景：科学计算、信号处理，日常编程很少用
  - 例子：`c = 3+5j`

- **str**（字符串）→ 文字内容，比如 `"hello"`, `"123"`
  - 使用场景：存储和处理文字，比如名字、输入、消息
  - 例子：`name = "Tom"`

- **bool**（布尔值）→ 只有两个值：`True` 或 `False`
  - 使用场景：条件判断、控制程序流程
  - 例子：`is_logged_in = True`

- **NoneType**（空值）→ 只有一个值：`None`，表示"什么都没有"
  - 使用场景：表示一个变量还没有值，或函数没有返回值
  - 例子：`result = None`

---

## 二、Python 所有数据结构

- **list**（列表）→ 有序、可变
  - 使用场景：需要按顺序存储一组数据，且之后可能会修改
  - 例子：`fruits = ["apple", "banana", "orange"]`

- **tuple**（元组）→ 有序、不可变
  - 使用场景：数据不需要修改，比如坐标、RGB颜色值
  - 例子：`position = (10, 20)`

- **dict**（字典）→ 键值对，可变
  - 使用场景：需要通过名字（key）来查找对应的值
  - 例子：`user = {"name": "Tom", "age": 18}`

- **set**（集合）→ 无序、不重复
  - 使用场景：需要去除重复数据，或判断某个值是否存在
  - 例子：`tags = {"python", "coding", "python"}  # 自动变成 {"python", "coding"}`

- **frozenset**（冻结集合）→ 和 set 一样，但不可变
  - 使用场景：需要一个不可修改的集合，比如作为 dict 的 key
  - 例子：`fs = frozenset({"python", "coding"})`

- **bytes**（字节序列）→ 存储二进制数据，不可变
  - 使用场景：处理文件、网络传输、图片等二进制内容
  - 例子：`data = b"hello"`

- **bytearray**（可变字节序列）→ 和 bytes 一样，但可变
  - 使用场景：需要修改二进制数据的场合
  - 例子：`ba = bytearray(b"hello")`

- **deque**（双端队列）→ 两端都可以快速插入和删除
  - 使用场景：需要频繁在头部或尾部添加/删除数据，比如排队系统
  - 例子：
    ```python
    from collections import deque
    q = deque([1, 2, 3])
    q.appendleft(0)   # 从左边加 → [0, 1, 2, 3]
    ```

- **heap**（堆）→ 自动保持最小值在最前面
  - 使用场景：需要反复取出最小值，比如任务优先级排序
  - 例子：
    ```python
    import heapq
    h = [3, 1, 2]
    heapq.heapify(h)
    print(heapq.heappop(h))   # 输出 1，永远取出最小值
    ```


    在 Python 中有几种方式判断一个数是否是 `int`：

**方法1：`isinstance()`（推荐）**
```python
x = 42
print(isinstance(x, int))   # True

y = 3.14
print(isinstance(y, int))   # False
```

**方法2：`type()`**
```python
x = 42
print(type(x) == int)   # True
print(type(x) is int)   # True

y = 3.14
print(type(y) == int)   # False
```

**`isinstance` vs `type` 的区别**
```python
# isinstance 对子类也返回 True（更灵活）
print(isinstance(True, int))    # True（bool 是 int 的子类）
print(type(True) == int)        # False
```

**方法3：判断字符串能否转为 int（用户输入场景）**
```python
s = "123"
print(s.isdigit())   # True

s2 = "12.3"
print(s2.isdigit())  # False
```

---

**推荐使用 `isinstance()`**，因为：
- 支持继承关系（子类判断）
- 可以同时判断多个类型：`isinstance(x, (int, float))`
- 是 Python 的惯用写法（Pythonic）


对！你的测试完美验证了之前说的：

**`//` 永远返回 `int`**，所以 `type(months // 7) == int` 永远是 `True`，用它来判断"是否整除"是**没有意义的**。

```python
months = 1
months // 7   # → 0  (int，但其实除不尽！)

months = 7
months // 7   # → 1  (int，整除了)
```

两种情况 `type()` 都是 `int`，无法区分。

---

**所以你真正需要的是 `%` 取余：**

```python
months = 1
print(months % 7)   # → 1  (有余数，除不尽)

months = 7
print(months % 7)   # → 0  (无余数，整除了)
```

```python
# 正确判断是否能被7整除
if months % 7 == 0:
    print("能被7整除")
else:
    print("不能被7整除")
```

`%` 才是判断整除的正确工具，不是 `type()`。