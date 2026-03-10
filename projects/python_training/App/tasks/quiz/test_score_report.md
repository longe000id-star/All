---
cssclasses:
  - oup-modern-large
---

←
←
# 书本密码 - 知识点测验 评分报告

## 一、选择题详细评分

### 题号: 1
- **用户答案**: C
- **正确答案**: C
- **得分**: 10分
- **错误原因**: 无
- **解析**: 字典推导式的正确格式是 `{key: value for item in iterable}`，使用花括号创建，可以包含条件但不是必须的。

### 题号: 2
- **用户答案**: B
- **正确答案**: B
- **得分**: 10分
- **错误原因**: 无
- **解析**: 代码将每个单词作为键，单词长度作为值，正确输出为 `{'apple': 5, 'banana': 6, 'cherry': 6}`。

### 题号: 3
- **用户答案**: C
- **正确答案**: C
- **得分**: 10分
- **错误原因**: 无
- **解析**: `string.find(char)` 方法返回字符在字符串中第一次出现的位置（从0开始），如果找不到返回-1。

### 题号: 4
- **用户答案**: B
- **正确答案**: B
- **得分**: 10分
- **错误原因**: 无
- **解析**: 'o'在位置4，'x'不存在返回-1。

### 题号: 5
- **用户答案**: B
- **正确答案**: B
- **得分**: 10分
- **错误原因**: 无
- **解析**: for循环中的变量名可以任意取，只要在循环体内一致使用即可。

## 二、填空题详细评分

### 题号: 6
- **用户答案**: `{numbers[i]: numbers[i] for i in range(len(numbers))}`
- **正确答案**: `{num: num**2 for num in numbers}`
- **得分**: 0分
- **错误原因**: 用户代码将数字作为键和值，没有计算平方
- **解析**: 需要使用 `num**2` 计算平方值作为字典的值

### 题号: 7
- **用户答案**: 
  - 第1次循环后: `{"a": 0}`
  - 第2次循环后：`{"a": 0, "b":1}`
  - 第3次循环后：`{"a": 2, "b":1}`
  - 第4次循环后：`{"a": 2, "b":1, "c": 3}`
  - 最终结果：`{"a": 2, "b":1, "c": 3}`
- **正确答案**: 
  - 第1次：`{'a': 0}`
  - 第2次：`{'a': 0, 'b': 1}`
  - 第3次：`{'a': 2, 'b': 1}` (a被覆盖)
  - 第4次：`{'a': 2, 'b': 1, 'c': 3}`
  - 最终：`{'a': 2, 'b': 1, 'c': 3}`
- **得分**: 10分
- **错误原因**: 无
- **解析**: 用户正确理解了字典键值对的覆盖机制，当遇到重复键时会更新值。

### 题号: 8
- **用户答案**: 
  ```python
  if not c in char_count.keys():
      char_count[c] = 1
  else:
      char_count[c] = char_count[c] + 1
  ```
- **正确答案**: 
  ```python
  if c in char_count:
      char_count[c] += 1
  else:
      char_count[c] = 1
  ```
- **得分**: 5分
- **错误原因**: 使用了冗余的 `.keys()` 方法，代码不够简洁
- **解析**: 可以直接使用 `if c in char_count` 检查键是否存在，使用 `+=` 操作符更简洁

## 三、代码阅读题详细评分

### 题号: 9
- **用户答案**: 
  ```
  第1次循环：{"p": "0"}
  第2次循环：{"p": "0", "o": "4'}
  第3次循环：{"p": "0", "o": "4'}
  最终结果：{"p": "0", "o": "4'}
  ```
- **正确答案**: 
  ```
  第1次：{'p': '0'}
  第2次：{'p': '0', 'o': '4'}
  第3次：{'p': '0', 'o': '4'} (p被覆盖)
  最终：{'p': '0', 'o': '4'}
  ```
- **得分**: 5分
- **错误原因**: 
  1. 字符串引号不匹配（使用了单引号）
  2. 第2次循环的字典格式错误
- **解析**: `book.find('p')` 返回0，`book.find('o')` 返回4，第三次循环时'p'被覆盖但值不变

### 题号: 10
- **用户答案**: `{'b':2, 'c':3}`
- **正确答案**: `{'b': 2, 'c': 3}`
- **得分**: 10分
- **错误原因**: 无
- **解析**: 字典推导式正确过滤了值大于1的键值对。

## 四、改错题详细评分

### 题号: 11
- **用户答案**: 
  ```python
  alphabet = "abc"
  letter_dict = {}
  for i in alphabet:
      letter_dict[i] = alphabet.find(i) # letter_dict{i} = alphabet.find(i)
  ```
- **正确答案**: 
  ```python
  alphabet = "abc"
  letter_dict = {}
  for i in alphabet:
      letter_dict[i] = alphabet.find(i)  # 修复：使用方括号而不是花括号
  ```
- **得分**: 5分
- **错误原因**: 用户指出了错误但没有完全改正
- **解析**: 错误是使用了花括号 `{}` 而不是方括号 `[]` 来访问字典

### 题号: 12
- **用户答案**: 
  ```python
  def create_mapping(book, text):
      mapping = {}
      for char in text:
          position = book.find[char]
          mapping[char] = str(position) # mapping.char = str(position)
      return mapping
  ```
- **正确答案**: 
  ```python
  def create_mapping(book, text):
      mapping = {}
      for char in text:  # 修复：添加冒号
          position = book.find(char)  # 修复：使用函数调用而不是索引
          mapping[char] = str(position)  # 修复：使用方括号访问字典
      return mapping
  ```
- **得分**: 0分
- **错误原因**: 用户没有提供完整的修复代码
- **解析**: 有三处错误：缺少冒号、错误使用方括号调用方法、错误使用点号访问字典

## 五、简答题详细评分

### 题号: 13
- **用户答案**: 
  ```
  result1 和 result2 区别在于 key, value 选择不同。result1 的 key 是 character，index 是 value；而 result2 正好相反。
  ```
- **正确答案**: 
  ```
  代码A创建的是字符到位置的映射（字符为键，位置为值）
  代码B创建的是位置到字符的映射（位置为键，字符为值）
  ```
- **得分**: 5分
- **错误原因**: 回答不够准确，result2的键是索引位置，值是字符
- **解析**: 两个代码的映射方向完全相反，这是字典推导式和普通循环创建字典的区别

### 题号: 14
- **用户答案**: 
  ```
  ❌ 因为有可能找不到，而返回 -1，......我一开始以为可能有负数，放在字典可能作为 int 可能不合适，所以要变成 string 格式？但是我后来试试 print（-1）的时候，又可以打印出来，所以其实这里不需要 str, 也可以运行吗？
  ```
- **正确答案**: 
  ```
  因为后续需要用星号拼接成字符串，整数不能直接参与字符串拼接
  ```
- **得分**: 0分
- **错误原因**: 回答完全错误，没有理解字符串拼接的需要
- **解析**: 在书本密码中，需要将位置数字转换为字符串以便进行字符串拼接操作

## 六、编程题详细评分

### 题号: 15
- **用户答案**: 
  ```python
  def reverse_dict(d):
      new_dict = {k: v for v, k in d.items()}
      return new_dict
  ```
- **正确答案**: 
  ```python
  def reverse_dict(d):
      return {v: k for k, v in d.items()}
  ```
- **得分**: 5分
- **错误原因**: 键值对顺序写反了
- **解析**: 应该是 `{v: k for k, v in d.items()}` 而不是 `{k: v for v, k in d.items()}`

### 题号: 16
- **用户答案**: 
  ```python
  def filter_dict(d, min_value):
      new_dict= {k: v for k, v in d.items() if v > min_value}
      return new_dict
      
  d = {'x': 12, 'y': 5, 'z': 18, 'w': 7, 'v': 10} 
  min_value = 9
  print(filter_dict(d, min_value))
  ```
- **正确答案**: 
  ```python
  def filter_dict(d, min_value):
      return {k: v for k, v in d.items() if v >= min_value}
  ```
- **得分**: 5分
- **错误原因**: 
  1. 使用了 `>` 而不是 `>=`（题目要求大于等于）
  2. 包含了测试代码，这不是题目要求的
- **解析**: 需要使用 `>=` 来包含等于最小值的情况

## 七、原代码错误详细分析

### 1. 语法错误
- **第6题**: 字典推导式语法错误，没有计算平方值
- **第11题**: 使用花括号 `{}` 而不是方括号 `[]` 访问字典
- **第12题**: 缺少冒号、错误使用方括号调用方法、错误使用点号访问字典

### 2. 逻辑错误
- **第8题**: 使用冗余的 `.keys()` 方法，代码不够简洁
- **第9题**: 字符串引号不匹配，字典格式错误
- **第13题**: 对字典映射方向理解不准确
- **第14题**: 完全误解了字符串转换的原因
- **第15题**: 键值对顺序颠倒
- **第16题**: 使用了错误的比较运算符（> 而不是 >=）

### 3. 概念理解错误
- **第14题**: 没有理解字符串拼接的需要
- **第13题**: 对字典推导式和普通循环创建字典的区别理解不清

## 八、参考答案代码

```python
# 第6题
numbers = [1, 2, 3, 4, 5]
square_dict = {num: num**2 for num in numbers}
print(square_dict)

# 第8题
sentence = "hello world"
char_count = {}
for c in sentence:
    if c != ' ':  # 忽略空格
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

# 第11题
alphabet = "abc"
letter_dict = {}
for i in alphabet:
    letter_dict[i] = alphabet.find(i)

# 第12题
def create_mapping(book, text):
    mapping = {}
    for char in text:
        position = book.find(char)
        mapping[char] = str(position)
    return mapping

# 第15题
def reverse_dict(d):
    return {v: k for k, v in d.items()}

# 第16题
def filter_dict(d, min_value):
    return {k: v for k, v in d.items() if v >= min_value}
```

## 九、总评

### 最终得分: 70分
### 等级: 中等
### 评语: 
用户在基础概念理解方面表现良好，能够正确回答大部分选择题。但在实际编程应用中存在一些问题，特别是在字典推导式的语法和逻辑上需要加强。对于字符串操作和字典访问的基本语法也有混淆。

### 改进建议:
1. **加强字典推导式练习**: 多练习 `{key: value for item in iterable}` 的各种变体
2. **注意语法细节**: 区分字典访问 `[]`、函数调用 `()`、和属性访问 `.`
3. **理解字符串拼接**: 掌握不同类型数据之间的转换和拼接规则
4. **练习条件判断**: 熟练使用 `>=`、`>` 等比较运算符的正确场景
5. **代码简洁性**: 学习使用更简洁的语法，如直接用 `if key in dict` 而不是 `if key in dict.keys()`