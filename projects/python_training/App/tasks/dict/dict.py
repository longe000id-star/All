←
←
number_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 10: 'ten'}
word_to_number = {w: d for d, w in number_to_word.items()}
print("反转字典:", word_to_number)


# 替代为普通函数版本（更容易理解）
def gen_code_keys(book, plain_text):
    """生成编码字典：将明文字符映射到它在书中首次出现的位置"""
    code_dict = {}
    for c in plain_text:
        position = book.find(c)           # 查找字符在书中的位置
        code_dict[c] = str(position)      # 将位置转为字符串并存入字典
    return code_dict

# 测试代码
book = "Once upon a time, in a house in a land far away,"
plain_text = "no is no"

# 调用函数
code_keys = gen_code_keys(book, plain_text)
print("编码字典:", code_keys)
# 输出: 编码字典: {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}



# ========== 第1次循环 ==========
def gen_code_keys(book, plain_text):
    code_dict = {}
    for c in plain_text:
        # 第1次: c = 'n' → 找 'n' 在 book 中的位置
        position = book.find(c)  # position = 1
        # 第1次: 把 'n':'1' 加入字典
        code_dict[c] = str(position)
        # 第1次后字典: {'n': '1'}
    return code_dict

# ========== 第2次循环 ==========
def gen_code_keys(book, plain_text):
    code_dict = {'n': '1'}
    for c in plain_text:
        # 第2次: c = 'o' → 找 'o' 在 book 中的位置
        position = book.find(c)  # position = 7
        # 第2次: 把 'o':'7' 加入字典
        code_dict[c] = str(position)
        # 第2次后字典: {'n': '1', 'o': '7'}
    return code_dict

# ========== 第3次循环 ==========
def gen_code_keys(book, plain_text):
    code_dict = {'n': '1', 'o': '7'}
    for c in plain_text:
        # 第3次: c = ' ' → 找 ' ' 在 book 中的位置
        position = book.find(c)  # position = 4
        # 第3次: 把 ' ':'4' 加入字典
        code_dict[c] = str(position)
        # 第3次后字典: {'n': '1', 'o': '7', ' ': '4'}
    return code_dict

# ========== 第4次循环 ==========
def gen_code_keys(book, plain_text):
    code_dict = {'n': '1', 'o': '7', ' ': '4'}
    for c in plain_text:
        # 第4次: c = 'i' → 找 'i' 在 book 中的位置
        position = book.find(c)  # position = 13
        # 第4次: 把 'i':'13' 加入字典
        code_dict[c] = str(position)
        # 第4次后字典: {'n': '1', 'o': '7', ' ': '4', 'i': '13'}
    return code_dict

# ========== 第5次循环 ==========
def gen_code_keys(book, plain_text):
    code_dict = {'n': '1', 'o': '7', ' ': '4', 'i': '13'}
    for c in plain_text:
        # 第5次: c = 's' → 找 's' 在 book 中的位置
        position = book.find(c)  # position = 26
        # 第5次: 把 's':'26' 加入字典
        code_dict[c] = str(position)
        # 第5次后字典: {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
    return code_dict

# ========== 第6次循环 ==========
def gen_code_keys(book, plain_text):
    code_dict = {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
    for c in plain_text:
        # 第6次: c = ' ' → 找 ' ' 在 book 中的位置
        position = book.find(c)  # position = 4
        # 第6次: 把 ' ':'4' 加入字典 (覆盖原来的)
        code_dict[c] = str(position)
        # 第6次后字典: {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
    return code_dict

# ========== 第7次循环 ==========
def gen_code_keys(book, plain_text):
    code_dict = {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
    for c in plain_text:
        # 第7次: c = 'n' → 找 'n' 在 book 中的位置
        position = book.find(c)  # position = 1
        # 第7次: 把 'n':'1' 加入字典 (覆盖原来的)
        code_dict[c] = str(position)
        # 第7次后字典: {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
    return code_dict

# ========== 第8次循环 ==========
def gen_code_keys(book, plain_text):
    code_dict = {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
    for c in plain_text:
        # 第8次: c = 'o' → 找 'o' 在 book 中的位置
        position = book.find(c)  # position = 7
        # 第8次: 把 'o':'7' 加入字典 (覆盖原来的)
        code_dict[c] = str(position)
        # 第8次后字典: {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
    return code_dict

# 最终返回: {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}



def encoder(code_keys, plain_text):
    # code_keys: 编码字典，比如 {'n':'1', 'o':'7', ' ':'4', 'i':'13', 's':'26'}
    # plain_text: 明文，比如 "no is no"
    
    # 第1步：列表推导式，把每个字符转换成 '*' + 对应的编码
    code_list = ['*' + code_keys[c] for c in plain_text]
    # 结果: ['*1', '*7', '*4', '*13', '*26', '*4', '*1', '*7']
    
    # 第2步：用 ''.join() 把列表拼接成字符串
    temp_string = ''.join(code_list)
    # 结果: '*1*7*4*13*26*4*1*7'
    
    # 第3步：[1:] 去掉开头的第一个星号
    final_result = temp_string[1:]
    # 结果: '1*7*4*13*26*4*1*7'
    
    return final_result

def encrypt(book, plain_text):
    # 第1步：生成编码字典
    code_keys = gen_code_keys(book, plain_text)
    # code_keys = {'n': '1', 'o': '7', ' ': '4', 'i': '13', 's': '26'}
    
    # 第2步：用编码字典加密明文
    cipher_text = encoder(code_keys, plain_text)
    # cipher_text = '1*7*4*13*26*4*1*7'
    
    return cipher_text

# ========== 原始数据 ==========
book = "Once upon a time, in a house in a land far away,"
plain_text = "no is no"

def encrypt(book, plain_text):
    # ========== 第1步：调用 gen_code_keys ==========
    code_keys = gen_code_keys(book, plain_text)
    # 进入 gen_code_keys 函数:
    #   第1次循环: c='n' → book.find('n')=1 → {'n':'1'}
    #   第2次循环: c='o' → book.find('o')=7 → {'n':'1', 'o':'7'}
    #   第3次循环: c=' ' → book.find(' ')=4 → {'n':'1', 'o':'7', ' ':'4'}
    #   第4次循环: c='i' → book.find('i')=13 → {'n':'1', 'o':'7', ' ':'4', 'i':'13'}
    #   第5次循环: c='s' → book.find('s')=26 → {'n':'1', 'o':'7', ' ':'4', 'i':'13', 's':'26'}
    #   第6次循环: c=' ' → book.find(' ')=4 → 不变
    #   第7次循环: c='n' → book.find('n')=1 → 不变
    #   第8次循环: c='o' → book.find('o')=7 → 不变
    # 返回: {'n':'1', 'o':'7', ' ':'4', 'i':'13', 's':'26'}
    
    # ========== 第2步：调用 encoder ==========
    cipher_text = encoder(code_keys, plain_text)
    # 进入 encoder 函数:
    #   列表推导式生成: ['*1', '*7', '*4', '*13', '*26', '*4', '*1', '*7']
    #   ''.join()后: '*1*7*4*13*26*4*1*7'
    #   [1:]去掉第一个星号: '1*7*4*13*26*4*1*7'
    # 返回: '1*7*4*13*26*4*1*7'
    
    return cipher_text

# 调用 encrypt
result = encrypt(book, plain_text)
print(result)  # '1*7*4*13*26*4*1*7'



# 第1步：生成编码字典
def gen_code_keys(book, plain_text):
    code_dict = {}
    for c in plain_text:
        position = book.find(c)
        code_dict[c] = str(position)
    return code_dict

# 第2步：编码器
def encoder(code_keys, plain_text):
    coded_list = ['*' + code_keys[c] for c in plain_text]
    return ''.join(coded_list)[1:]

# 第3步：加密函数
def encrypt(book, plain_text):
    code_keys = gen_code_keys(book, plain_text)
    cipher_text = encoder(code_keys, plain_text)
    return cipher_text

# 测试
book = "Once upon a time, in a house in a land far away,"
plain_text = "no is no"

result = encrypt(book, plain_text)
print(f"明文: '{plain_text}'")
print(f"密文: '{result}'")


def gen_decode_keys(book, cipher_text):
    # cipher_text: 收到的密文，比如 "1*7*4*13*26*4*1*7"
    # book: 同一本书 "Once upon a time..."
    
    # 第1步：用 split('*') 把密文按星号拆分成列表
    number_list = cipher_text.split('*')
    # 结果: ['1', '7', '4', '13', '26', '4', '1', '7']
    
    # 第2步：遍历每个数字字符串
    decode_dict = {}
    for s in number_list:
        # s 是字符串形式的数字，比如 '1', '7', '4'...
        index = int(s)        # 把字符串转成整数，比如 '1' → 1
        character = book[index]  # 在书中取出对应位置的字符
        decode_dict[s] = character  # 键是数字字符串，值是字符
    
    return decode_dict

# ========== 原始数据 ==========
book = "Once upon a time, in a house in a land far away,"
cipher_text = "1*7*4*13*26*4*1*7"

def gen_decode_keys(book, cipher_text):
    # ========== 第1步：拆分密文 ==========
    number_list = cipher_text.split('*')
    # number_list = ['1', '7', '4', '13', '26', '4', '1', '7']
    
    # ========== 初始化空字典 ==========
    decode_dict = {}
    
    # ========== 第1次循环 ==========
    # 当前字典: {}
    for s in number_list:
        # 第1次: s = '1' → int('1') = 1 → book[1] = 'n'
        # 第1次后字典: {'1': 'n'}
    
    # ========== 第2次循环 ==========
    # 当前字典: {'1': 'n'}
    for s in number_list:
        # 第2次: s = '7' → int('7') = 7 → book[7] = 'o'
        # 第2次后字典: {'1': 'n', '7': 'o'}
    
    # ========== 第3次循环 ==========
    # 当前字典: {'1': 'n', '7': 'o'}
    for s in number_list:
        # 第3次: s = '4' → int('4') = 4 → book[4] = ' '
        # 第3次后字典: {'1': 'n', '7': 'o', '4': ' '}
    
    # ========== 第4次循环 ==========
    # 当前字典: {'1': 'n', '7': 'o', '4': ' '}
    for s in number_list:
        # 第4次: s = '13' → int('13') = 13 → book[13] = 'i'
        # 第4次后字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i'}
    
    # ========== 第5次循环 ==========
    # 当前字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i'}
    for s in number_list:
        # 第5次: s = '26' → int('26') = 26 → book[26] = 's'
        # 第5次后字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}
    
    # ========== 第6次循环 ==========
    # 当前字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}
    for s in number_list:
        # 第6次: s = '4' → int('4') = 4 → book[4] = ' ' (覆盖，和之前一样)
        # 第6次后字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}
    
    # ========== 第7次循环 ==========
    # 当前字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}
    for s in number_list:
        # 第7次: s = '1' → int('1') = 1 → book[1] = 'n' (覆盖，和之前一样)
        # 第7次后字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}
    
    # ========== 第8次循环 ==========
    # 当前字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}
    for s in number_list:
        # 第8次: s = '7' → int('7') = 7 → book[7] = 'o' (覆盖，和之前一样)
        # 第8次后字典: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}
    
    return decode_dict
    # 返回: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}



def gen_decode_keys(book, cipher_text):
    # 按星号拆分密文，得到数字列表
    numbers = cipher_text.split('*')
    
    # 对每个数字，从书中取出对应字符
    decode_dict = {}
    for num_str in numbers:
        index = int(num_str)
        decode_dict[num_str] = book[index]
    
    return decode_dict

# 测试
book = "Once upon a time, in a house in a land far away,"
cipher_text = "1*7*4*13*26*4*1*7"

decode_keys = gen_decode_keys(book, cipher_text)
print(decode_keys)
# 输出: {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}



## 第六步：理解解码器函数 decoder 和完整的解密函数 decrypt

```python
# 原文中的 decoder 函数（需要我们自己实现）
# 使用模型：参考 encoder 的结构
```

### 先回忆 encoder 是怎么做的

```python
def encoder(code_keys, plain_text):
    # code_keys: {'n':'1', 'o':'7', ' ':'4', 'i':'13', 's':'26'}
    # plain_text: "no is no"
    
    # 把每个字符替换成对应的编码，前面加星号
    coded_list = ['*' + code_keys[c] for c in plain_text]
    # 结果: ['*1', '*7', '*4', '*13', '*26', '*4', '*1', '*7']
    
    # 拼接并去掉开头的星号
    return ''.join(coded_list)[1:]
    # 返回: '1*7*4*13*26*4*1*7'
```

### 现在实现 decoder（反向操作）

```python
def decoder(decode_keys, cipher_text):
    # decode_keys: {'1':'n', '7':'o', '4':' ', '13':'i', '26':'s'}
    # cipher_text: "1*7*4*13*26*4*1*7"
    
    # 第1步：按星号拆分密文
    number_list = cipher_text.split('*')
    # number_list = ['1', '7', '4', '13', '26', '4', '1', '7']
    
    # 第2步：把每个数字替换成对应的字符
    char_list = [decode_keys[s] for s in number_list]
    # 第1次: s='1' → decode_keys['1']='n' → ['n']
    # 第2次: s='7' → decode_keys['7']='o' → ['n','o']
    # 第3次: s='4' → decode_keys['4']=' ' → ['n','o',' ']
    # 第4次: s='13' → decode_keys['13']='i' → ['n','o',' ','i']
    # 第5次: s='26' → decode_keys['26']='s' → ['n','o',' ','i','s']
    # 第6次: s='4' → decode_keys['4']=' ' → ['n','o',' ','i','s',' ']
    # 第7次: s='1' → decode_keys['1']='n' → ['n','o',' ','i','s',' ','n']
    # 第8次: s='7' → decode_keys['7']='o' → ['n','o',' ','i','s',' ','n','o']
    
    # 第3步：拼接成字符串
    return ''.join(char_list)
    # 返回: 'no is no'
```

### 一步步拆解 decoder 执行过程

```python
# ========== 原始数据 ==========
decode_keys = {'1': 'n', '7': 'o', '4': ' ', '13': 'i', '26': 's'}
cipher_text = "1*7*4*13*26*4*1*7"

def decoder(decode_keys, cipher_text):
    # ========== 第1步：拆分 ==========
    number_list = cipher_text.split('*')
    # number_list = ['1', '7', '4', '13', '26', '4', '1', '7']
    
    # ========== 初始化空列表 ==========
    char_list = []
    
    # ========== 第1次循环 ==========
    # 当前列表: []
    for s in number_list:
        # 第1次: s = '1' → decode_keys['1'] = 'n' → 加入列表
        # 第1次后列表: ['n']
    
    # ========== 第2次循环 ==========
    # 当前列表: ['n']
    for s in number_list:
        # 第2次: s = '7' → decode_keys['7'] = 'o' → 加入列表
        # 第2次后列表: ['n', 'o']
    
    # ========== 第3次循环 ==========
    # 当前列表: ['n', 'o']
    for s in number_list:
        # 第3次: s = '4' → decode_keys['4'] = ' ' → 加入列表
        # 第3次后列表: ['n', 'o', ' ']
    
    # ========== 第4次循环 ==========
    # 当前列表: ['n', 'o', ' ']
    for s in number_list:
        # 第4次: s = '13' → decode_keys['13'] = 'i' → 加入列表
        # 第4次后列表: ['n', 'o', ' ', 'i']
    
    # ========== 第5次循环 ==========
    # 当前列表: ['n', 'o', ' ', 'i']
    for s in number_list:
        # 第5次: s = '26' → decode_keys['26'] = 's' → 加入列表
        # 第5次后列表: ['n', 'o', ' ', 'i', 's']
    
    # ========== 第6次循环 ==========
    # 当前列表: ['n', 'o', ' ', 'i', 's']
    for s in number_list:
        # 第6次: s = '4' → decode_keys['4'] = ' ' → 加入列表
        # 第6次后列表: ['n', 'o', ' ', 'i', 's', ' ']
    
    # ========== 第7次循环 ==========
    # 当前列表: ['n', 'o', ' ', 'i', 's', ' ']
    for s in number_list:
        # 第7次: s = '1' → decode_keys['1'] = 'n' → 加入列表
        # 第7次后列表: ['n', 'o', ' ', 'i', 's', ' ', 'n']
    
    # ========== 第8次循环 ==========
    # 当前列表: ['n', 'o', ' ', 'i', 's', ' ', 'n']
    for s in number_list:
        # 第8次: s = '7' → decode_keys['7'] = 'o' → 加入列表
        # 第8次后列表: ['n', 'o', ' ', 'i', 's', ' ', 'n', 'o']
    
    # ========== 拼接字符串 ==========
    result = ''.join(['n', 'o', ' ', 'i', 's', ' ', 'n', 'o'])
    # result = 'no is no'
    
    return result
```

### 现在实现完整的 decrypt 函数

```python
def decrypt(book, cipher_text):
    # 第1步：生成解码字典
    decode_keys = gen_decode_keys(book, cipher_text)
    # decode_keys = {'1':'n', '7':'o', '4':' ', '13':'i', '26':'s'}
    
    # 第2步：用解码字典解密密文
    plain_text = decoder(decode_keys, cipher_text)
    # plain_text = 'no is no'
    
    return plain_text
```

### 所有函数放在一起

```python
# 编码相关
def gen_code_keys(book, plain_text):
    code_dict = {}
    for c in plain_text:
        code_dict[c] = str(book.find(c))
    return code_dict

def encoder(code_keys, plain_text):
    coded_list = ['*' + code_keys[c] for c in plain_text]
    return ''.join(coded_list)[1:]

def encrypt(book, plain_text):
    code_keys = gen_code_keys(book, plain_text)
    return encoder(code_keys, plain_text)

# 解码相关
def gen_decode_keys(book, cipher_text):
    decode_dict = {}
    for s in cipher_text.split('*'):
        decode_dict[s] = book[int(s)]
    return decode_dict

def decoder(decode_keys, cipher_text):
    char_list = [decode_keys[s] for s in cipher_text.split('*')]
    return ''.join(char_list)

def decrypt(book, cipher_text):
    decode_keys = gen_decode_keys(book, cipher_text)
    return decoder(decode_keys, cipher_text)

# 测试
book = "Once upon a time, in a house in a land far away,"
plain_text = "no is no"

# 加密
cipher = encrypt(book, plain_text)
print(f"密文: {cipher}")

# 解密
decrypted = decrypt(book, cipher)
print(f"解密后: '{decrypted}'")
```

输出：
```
密文: 1*7*4*13*26*4*1*7
解密后: 'no is no'
```

要继续第七步（解决 finger exercise 的问题）吗？

