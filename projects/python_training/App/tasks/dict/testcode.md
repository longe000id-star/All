---
cssclasses:
  - oup-modern-large
---

←
←
# 书本密码 - 编码专题测验

## 一、选择题

### 1. 关于 `gen_code_keys` 函数，下列说法正确的是？
```python
def gen_code_keys(book, plain_text):
    code_dict = {}
    for c in plain_text:
        code_dict[c] = str(book.find(c))
    return code_dict
```
A) 函数返回的是字符到字符的映射
B) 函数返回的是字符到数字位置的映射（数字是字符串形式）
C) 函数返回的是数字位置到字符的映射
D) 函数返回的是字符在书中出现的次数

### 2. 阅读以下代码：
```python
book = "hello world"
plain_text = "hl"
result = gen_code_keys(book, plain_text)
print(result)
```
输出结果是？
A) `{'h': '0', 'l': '2'}`
B) `{'h': 0, 'l': 2}`
C) `{0: 'h', 2: 'l'}`
D) `{'h': 'hello', 'l': 'world'}`

### 3. 关于 `encoder` 函数，下列说法正确的是？
```python
def encoder(code_keys, plain_text):
    coded_list = ['*' + code_keys[c] for c in plain_text]
    return ''.join(coded_list)[1:]
```
A) 函数返回的字符串开头一定有星号
B) 函数返回的字符串中，每个编码之间用星号分隔，但开头没有星号
C) 函数返回的是列表
D) 函数会修改原始的 code_keys 字典

### 4. 如果 `code_keys = {'a':'5', 'b':'3'}`，`plain_text = "ab"`，`encoder` 函数的返回值是？
A) `'*5*3'`
B) `'5*3'`
C) `'*a*b'`
D) `'ab'`

### 5. 关于 `encrypt` 函数，下列说法正确的是？
```python
def encrypt(book, plain_text):
    code_keys = gen_code_keys(book, plain_text)
    return encoder(code_keys, plain_text)
```
A) 函数直接使用 book 作为编码字典
B) 函数先调用 gen_code_keys 生成编码字典，再用 encoder 加密
C) 函数只返回编码字典，不返回密文
D) 函数需要两个编码字典才能工作

---

## 二、填空题

### 6. 完成以下代码，实现 `encoder` 函数的每一步处理：
```python
code_keys = {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
plain_text = "no is no"

# 第1步：列表推导式，每个字符前加星号
coded_list = ['*' + code_keys[c] for c in plain_text]
# coded_list = _________________________________

# 第2步：拼接成字符串
temp_string = ''.join(coded_list)
# temp_string = _________________________________

# 第3步：去掉第一个星号
final_result = temp_string[1:]
# final_result = _________________________________
```

### 7. 阅读以下代码，写出每一步循环后的列表状态：
```python
code_keys = {'a': '0', 'b': '1', 'c': '2'}
plain_text = "abc"
coded_list = []

# 第1次循环
for c in plain_text:
    # 第1次: c = 'a' → '*' + code_keys['a'] = '*0'
    coded_list.append('*' + code_keys[c])
    # 第1次后列表: _________

# 第2次循环
    # 第2次: c = 'b' → '*' + code_keys['b'] = '*1'
    # 第2次后列表: _________

# 第3次循环
    # 第3次: c = 'c' → '*' + code_keys['c'] = '*2'
    # 第3次后列表: _________

# 最终列表: _________
# ''.join(最终列表) = _________
# [1:]去掉第一个星号后 = _________
```

### 8. 补全以下代码，实现加密过程的完整追踪：
```python
book = "python"
plain_text = "no"

def trace_encrypt(book, plain_text):
    print("=" * 40)
    print("开始加密过程")
    print("=" * 40)
    
    # 第1步：生成编码字典
    print("\n第1步：生成编码字典")
    code_dict = {}
    for c in plain_text:
        pos = book.find(c)
        code_dict[c] = str(pos)
        print(f"  字符 '{c}' → book.find('{c}') = {pos} → code_dict['{c}'] = '{pos}'")
        print(f"  当前字典: {code_dict}")
    
    print(f"\n  最终编码字典: {code_dict}")
    
    # 第2步：加密
    print("\n第2步：加密")
    coded_list = []
    for c in plain_text:
        item = _________________________  # '*' + 编码
        coded_list.append(item)
        print(f"  字符 '{c}' → 添加 '{item}' → 当前列表: {coded_list}")
    
    print(f"\n  最终列表: {coded_list}")
    
    temp = ''.join(coded_list)
    print(f"  拼接后: '{temp}'")
    
    result = _________________________  # 去掉第一个星号
    print(f"  去掉开头星号: '{result}'")
    
    print("\n" + "=" * 40)
    print(f"最终密文: '{result}'")
    print("=" * 40)
    
    return result

trace_encrypt(book, plain_text)
```

---

## 三、代码阅读题

### 9. 阅读以下代码，写出每一步的输出：
```python
book = "programming"
plain_text = "ram"

def step_by_step_encode(book, text):
    print(f"书: '{book}'")
    print(f"明文: '{text}'")
    print()
    
    # 生成编码字典
    code_dict = {}
    print("生成编码字典:")
    for c in text:
        pos = book.find(c)
        code_dict[c] = str(pos)
        print(f"  '{c}' → {pos} → code_dict['{c}'] = '{pos}'")
    
    print(f"\n编码字典: {code_dict}")
    print()
    
    # 加密
    print("加密过程:")
    coded_list = []
    for c in text:
        item = '*' + code_dict[c]
        coded_list.append(item)
        print(f"  添加 '{item}' → {coded_list}")
    
    temp = ''.join(coded_list)
    print(f"\n拼接: '{temp}'")
    
    result = temp[1:]
    print(f"结果: '{result}'")
    
    return result

result = step_by_step_encode(book, plain_text)
```

请写出程序输出：

```
书: 'programming'
明文: 'ram'

生成编码字典:
  _________
  _________
  _________

编码字典: _________

加密过程:
  _________
  _________
  _________

拼接: _________
结果: _________
```

### 10. 以下代码的输出是什么？
```python
def mystery_encode(book, text):
    code_dict = {c: str(book.find(c)) for c in text}
    print("编码字典:", code_dict)
    
    cipher = ''.join(['*' + code_dict[c] for c in text])[1:]
    return cipher

book = "abcdefg"
text = "age"
result = mystery_encode(book, text)
print("密文:", result)
```

输出：
```
编码字典: _________
密文: _________
```

---

## 四、改错题

### 11. 找出以下代码中的错误：
```python
def encode_message(book, text):
    code_keys = {}
    for char in text
        position = book.find[char]
        code_keys(char) = position
    return code_keys
```

### 12. 以下代码试图加密消息，但结果不对，请找出错误：
```python
book = "hello world"
plain = "hold"

code_dict = {}
for c in plain:
    code_dict[c] = book.find(c)

# 期望得到类似 "0*4*3*?" 的格式
cipher = ''
for c in plain:
    cipher += code_dict[c] + '*'

print(cipher)  # 输出: '0*4*3*-1*' （多了一个星号且没有去掉开头星号）
```

---

## 五、简答题

### 13. 解释为什么在 `encoder` 函数中要先用列表推导式生成 `['*1', '*7', ...]`，然后再 `''.join()`，最后 `[1:]`，而不是直接拼接字符串？

### 14. 在以下代码中，如果 `plain_text` 中有重复字符（如 "noon"），`code_dict` 会发生什么变化？这对最终的密文有影响吗？
```python
code_dict = {c: str(book.find(c)) for c in plain_text}
```

---

## 六、编程题

### 15. 编写一个函数 `show_encoding_steps(book, plain_text)`，该函数会详细打印出加密的每一步：
- 打印每个字符的查找位置
- 打印每次循环后的编码字典
- 打印列表推导式的每一步
- 打印最终的密文



### 16. 实现一个函数 `custom_encoder(code_keys, plain_text, separator)`，允许用户自定义分隔符（默认是 `'*'`），并且可以选择是否在开头保留分隔符。

示例：


---

## 参考答案

1. B
2. A
3. B
4. B
5. B

6. 
   - `['*1', '*7', '*4', '*13', '*26', '*4', '*1', '*7']`
   - `'*1*7*4*13*26*4*1*7'`
   - `'1*7*4*13*26*4*1*7'`

7. 
   - 第1次后: `['*0']`
   - 第2次后: `['*0', '*1']`
   - 第3次后: `['*0', '*1', '*2']`
   - 最终列表: `['*0', '*1', '*2']`
   - `''.join` = `'*0*1*2'`
   - `[1:]`后 = `'0*1*2'`

8. 
   - `item = '*' + code_dict[c]`
   - `result = temp[1:]`

9. 
   ```
   书: 'programming'
   明文: 'ram'

   生成编码字典:
     'r' → 2 → code_dict['r'] = '2'
     'a' → 8 → code_dict['a'] = '8'
     'm' → 5 → code_dict['m'] = '5'

   编码字典: {'r': '2', 'a': '8', 'm': '5'}

   加密过程:
     添加 '*2' → ['*2']
     添加 '*8' → ['*2', '*8']
     添加 '*5' → ['*2', '*8', '*5']

   拼接: '*2*8*5'
   结果: '2*8*5'
   ```

10. 
    ```
    编码字典: {'a': '0', 'g': '6', 'e': '4'}
    密文: '0*6*4'
    ```

11. 三处错误：
    - 缺少冒号：`for char in text:`
    - 错误使用方括号：`book.find(char)` 不是 `book.find[char]`
    - 错误使用括号：应该是 `code_keys[char] = position` 不是 `code_keys(char) = position`

12. 两处错误：
    - 没有去掉最后一个多余的星号
    - 没有在开头添加星号（根据原题格式要求）
    改正：
    ```python
    cipher = ''
    for c in plain:
        cipher += '*' + str(code_dict[c])
    cipher = cipher[1:]  # 去掉开头星号
    ```

13. 因为直接字符串拼接效率低（字符串不可变，每次拼接都会创建新字符串），用列表收集再 join 效率更高。先加星号再统一去掉第一个，是为了代码简洁，避免在循环中判断是否是第一个字符。

14. 重复字符在字典中只会保留最后一次出现的位置（后面的覆盖前面的）。但这不影响最终密文，因为加密时用的是 plain_text 的顺序，直接从 code_dict 取值，而 code_dict 中该字符对应的值（位置）是唯一的。

15. 
    ```python
    def show_encoding_steps(book, plain_text):
        print(f"书: '{book}'")
        print(f"明文: '{plain_text}'\n")
        
        # 生成编码字典
        print("生成编码字典:")
        code_dict = {}
        for c in plain_text:
            pos = book.find(c)
            code_dict[c] = str(pos)
            print(f"  字符 '{c}': book.find('{c}') = {pos} → 添加到字典 {code_dict}")
        
        print(f"\n最终编码字典: {code_dict}\n")
        
        # 加密
        print("加密列表生成:")
        coded_list = []
        for c in plain_text:
            item = '*' + code_dict[c]
            coded_list.append(item)
            print(f"  字符 '{c}' → '{item}' → {coded_list}")
        
        print(f"\n最终列表: {coded_list}")
        temp = ''.join(coded_list)
        print(f"拼接: '{temp}'")
        result = temp[1:]
        print(f"去掉开头星号: '{result}'")
        
        return result
    ```

16. 
    ```python
    def custom_encoder(code_keys, plain_text, separator='*', keep_first=False):
        coded_list = []
        for c in plain_text:
            if keep_first and len(coded_list) == 0:
                coded_list.append(separator + code_keys[c])
            else:
                coded_list.append(code_keys[c])
        
        if keep_first:
            return ''.join(coded_list)
        else:
            return separator.join(coded_list)
    ```