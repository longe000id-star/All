←
←
# 书本密码 - 知识点测验

## 一、选择题

### 1. 关于字典推导式，下列说法正确的是？(C)
A) 使用方括号 `[]` 创建
B) 必须包含 if 条件
C) 格式是 `{key: value for item in iterable}`
D) 只能用于字符串

### 2. 阅读以下代码：(B)
```python
words = ["apple", "banana", "cherry"]
result = {word: len(word) for word in words}
print(result)
```
输出结果是？(B)
A) `{0: 'apple', 1: 'banana', 2: 'cherry'}`
B) `{'apple': 5, 'banana': 6, 'cherry': 6}`
C) `{5: 'apple', 6: 'banana', 6: 'cherry'}`
D) `['apple', 'banana', 'cherry']`

### 3. 关于 `string.find(char)` 方法，下列说法正确的是？(C)
A) 返回字符在字符串中最后一次出现的位置
B) 如果找不到字符，返回 0
C) 返回字符在字符串中第一次出现的位置（从0开始）
D) 只能查找单个字符，不能查找子串

### 4. 分析以下代码：
```python
text = "hello world"
print(text.find('o'))
print(text.find('x'))
```
输出结果是？(B) # ❌ D
A) 4 和 0
B) 4 和 -1
C) 5 和 -1
D) 4 和 None

### 5. 关于 for 循环中的变量名，下列说法正确的是？(B)
A) 必须使用 c 作为变量名
B) 变量名可以任意取，只要在循环体内一致使用
C) 变量名必须是单个字母
D) 变量名必须在循环前预先定义

---

## 二、填空题

### 6. 完成以下字典推导式，将数字列表转换为字典（数字本身作为键，它的平方作为值）：
```python
numbers = [1, 2, 3, 4, 5]
square_dict = {numbers[i]: numbers[i] for i in range(len(numbers))}
print(square_dict)
_________________________
# 期望输出: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### 7. 阅读以下代码，写出每一步循环后的字典状态：
```python
text = "abac"
char_positions = {}
for index, c in enumerate(text):
    char_positions[c] = index
```
第1次循环后: char_positions = {"a": 0} 

第2次循环后：char_positions = {"a": 0, "b":1}

第3次循环后：char_positions = {"a": 2, "b":1}

第4次循环后：char_positions = {"a": 2, "b":1, "c": 3}

最终结果：char_positions = {"a": 2, "b":1, "c": 3}

### 8. 补全代码，统计字符串中每个字母出现的次数：
```python
sentence = "hello world"
char_count = {}
for c in sentence:
    if c != ' ':  # 忽略空格
        if not c in char_count.keys():
            char_count[c] = 1
        else:
            char_count[c] = char_count[c] + 1
    else:
        continue
```

---

## 三、代码阅读题

### 9. 阅读以下代码，写出执行过程：
```python
book = "python programming"
text = "pop"

def encode(book, text):
    code_dict = {}
    for c in text:
        pos = book.find(c)
        code_dict[c] = str(pos)
        print(f"当前字典: {code_dict}")
    return code_dict

result = encode(book, text)
print(f"最终结果: {result}")
```
```python
请写出每一步的输出： 

第1次循环：{"p": "0"} # ❌{"p": "1"} 

第2次循环：{"p": "0", "o": "4'}  # ❌{"p": "1", "o": "4'}

第3次循环：{"p": "0", "o": "4'} # ❌{"p": "1", "o": "4', "p": "1"}

最终结果：{"p": "0", "o": "4'}  # ❌ {"p": "1", "o": "4', "p": "1"}

```

### 10. 以下代码的输出是什么？
```python
data = [('a', 1), ('b', 2), ('c', 3)]
result = {k: v for k, v in data if v > 1}
print(result)
```
输出结果：{'b':2, 'c':3}


## 四、改错题

### 11. 以下代码试图创建字母表字典（a:0, b:1, c:2...），请找出错误并改正：
```python
alphabet = "abc"
letter_dict = {}
for i in alphabet:
    letter_dict[i] = alphabet.find(i) # letter_dict{i} = alphabet.find(i)
```

### 12. 找出以下代码中的错误：
```python
def create_mapping(book, text):
    mapping = {}
    for char in text:
        position = book.find[char]
        mapping[char] = str(position) # mapping.char = str(position)
    return mapping
```

---

## 五、简答题

### 13. 解释为什么以下两段代码的输出不同：
```python
# 代码A
text = "hello"
result1 = {c: text.find(c) for c in text}
print(result1)

result1 = {"h":0, "e":1, "l":3, "0":4}

# 代码B
result2 = {}
for i, c in enumerate(text):
    result2[i] = c
print(result2)

result2 = {0: "h", 1: "e", 2: "l", 4: "l", 5: "o"}
 result1 和 result2 区别在于 key, value 选择不同。result1 的 key 是 character，index 是 value；而 result2 正好相反。 

```

### 14. 在书本密码中，为什么需要用 `str(book.find(c))` 而不是直接使用整数？

> ❌ 因为有可能找不到，而返回 -1，......我一开始以为可能有负数，放在字典可能作为 int 可能不合适，所以要变成 string 格式？但是我后来试试 print（-1）的时候，又可以打印出来，所以其实这里不需要 str, 也可以运行吗？ 
---

## 六、编程题

### 15. 编写一个函数 `reverse_dict(d)`，接收一个字典作为参数，返回一个新的字典，其中原字典的键和值互换。

```python
def reverse_dict(d):
    new_dict = {k: v for v, k in d.items()}
    return new_dict

```


### 16. 编写一个函数 `filter_dict(d, min_value)`，只保留字典中值大于等于 min_value 的键值对

```python
def filter_dict(d, min_value):
    new_dict= {k: v for k, v in d.items() if v > min_value}
    return new_dict
    
d = {'x': 12, 'y': 5, 'z': 18, 'w': 7, 'v': 10} 
min_value = 9
print(filter_dict(d, min_value))


```



---

## 参考答案

1. C
2. B
3. C
4. B
5. B
6. `{num: num**2 for num in numbers}`
7. 
   - 第1次：`{'a': 0}`
   - 第2次：`{'a': 0, 'b': 1}`
   - 第3次：`{'a': 2, 'b': 1}` (a被覆盖)
   - 第4次：`{'a': 2, 'b': 1, 'c': 3}`
   - 最终：`{'a': 2, 'b': 1, 'c': 3}`
8. 
   ```python
   if c in char_count:
       char_count[c] += 1
   else:
       char_count[c] = 1
   ```
9. 
   - 第1次：`{'p': '0'}`
   - 第2次：`{'p': '0', 'o': '4'}`
   - 第3次：`{'p': '0', 'o': '4'}` (p被覆盖)
   - 最终：`{'p': '0', 'o': '4'}`
10. `{'b': 2, 'c': 3}`
11. 错误：使用了 `{}` 而不是 `[]`，应该用 `letter_dict[i] = alphabet.find(i)`
12. 三处错误：
    - 缺少冒号：`for char in text:`
    - 错误使用方括号：`book.find(char)` 不是 `book.find[char]`
    - 错误使用点号：应该是 `mapping[char] = ...` 不是 `mapping.char = ...`
13. 代码A创建的是字符到位置的映射，代码B创建的是位置到字符的映射
14. 因为后续需要用星号拼接成字符串，整数不能直接参与字符串拼接
15. 
    ```python
    def reverse_dict(d):
        return {v: k for k, v in d.items()}
    ```
16. 
    ```python
    def filter_dict(d, min_value):
        return {k: v for k, v in d.items() if v >= min_value}
    ```