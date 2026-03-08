←
←
# Python字典综合运用测验

## 测验说明
- 本测验共10题，难度由浅入深
- 每题包含：已知数据、任务说明、要求
- 请独立完成代码编写，答案在最后

---

## 第1题：创建数字映射字典

**已知数据**：
```python
numbers = [2, 4, 6, 8, 10, 12]
```

**任务说明**：创建一个字典，键为列表中的数字，值为该数字的立方。

**要求**：使用字典推导式一行完成

**预期结果**：一个字典，每个偶数数字映射到它的立方值
# 结果: {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000, 12: 1728}

---

## 第2题：统计字符串中字符出现次数

**已知数据**：
```python
text = "hello world python programming"
```

**任务说明**：统计字符串中每个字符出现的次数（忽略空格）

**要求**：分别用两种方法实现（if-else方法和get方法），返回两个字典

**预期结果**：一个字典，键为字符，值为该字符在字符串中出现的次数（空格不计）
# 结果示例: {'h': 2, 'e': 2, 'l': 4, 'o': 4, 'w': 1, 'r': 3, 'd': 2, 
#           'p': 2, 'y': 1, 't': 2, 'n': 3, 'g': 2, 'm': 2, 'a': 1, 'i': 1}
---

## 第3题：合并两个列表为字典

**已知数据**：
```python
cities = ["北京", "上海", "广州", "深圳", "杭州"]
populations = [2189, 2487, 1867, 1756, 1193]  # 单位：万人
```

**任务说明**：将城市名称和人口数据合并成字典

**要求**：分别用三种方法实现（zip+dict、字典推导式、for循环）

**预期结果**：一个字典，键为城市名，值为对应的人口数
# 结果: {'北京': 2189, '上海': 2487, '广州': 1867, '深圳': 1756, '杭州': 1193}
---

## 第4题：字典键值互换

**已知数据**：
```python
original = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'black': '#000000', 'white': '#FFFFFF'}
```

**任务说明**：交换字典的键和值，将颜色代码作为键，颜色名称作为值

**要求**：处理可能出现的重复值情况（本题中无重复，但代码要能处理）

**预期结果**：一个字典，键为颜色代码，值为颜色名称

---
# 结果: {'#FF0000': 'red', '#00FF00': 'green', '#0000FF': 'blue', 
#       '#000000': 'black', '#FFFFFF': 'white'}
## 第5题：筛选字典元素

**已知数据**：
```python
scores = {
    '语文': 85, '数学': 92, '英语': 78, '物理': 88, '化学': 65,
    '生物': 72, '历史': 58, '地理': 63, '政治': 71, '体育': 95
}
```

**任务说明**：筛选出成绩在60到90之间（包含60和90）的科目

**要求**：返回新字典，不修改原字典

**预期结果**：一个字典，只包含成绩在及格线以上但不超过90分的科目
# 结果: {'语文': 85, '英语': 78, '物理': 88, '化学': 65, 
#       '生物': 72, '地理': 63, '政治': 71}
---

## 第6题：按数值区间分组

**已知数据**：
```python
ages = [5, 12, 17, 23, 31, 45, 52, 68, 71, 84, 3, 15, 27, 33, 49, 55, 62, 77, 93]
```

**任务说明**：将年龄按区间分组：0-18（未成年）、19-35（青年）、36-55（中年）、56及以上（老年）

**要求**：返回一个字典，键为区间名称，值为该区间的年龄列表

**预期结果**：一个包含四个键的字典，每个键对应一个年龄列表
# 结果: {'未成年': [5, 12, 17, 3, 15], '青年': [23, 31, 27, 33], 
#       '中年': [45, 52, 49, 55], '老年': [68, 71, 84, 62, 77, 93]}
---

## 第7题：购物车商品统计

**已知数据**：
```python
orders = [
    {'商品': '苹果', '价格': 8, '数量': 3},
    {'商品': '香蕉', '价格': 5, '数量': 2},
    {'商品': '苹果', '价格': 8, '数量': 1},
    {'商品': '橙子', '价格': 6, '数量': 4},
    {'商品': '香蕉', '价格': 5, '数量': 3},
    {'商品': '葡萄', '价格': 12, '数量': 1},
    {'商品': '苹果', '价格': 8, '数量': 2}
]
```

**任务说明**：统计每种商品的总数量和总金额

**要求**：返回一个字典，键为商品名，值为[总数量, 总金额]

**预期结果**：一个字典，汇总每种商品的购买总量和总花费

# 结果: 
# {
#     '苹果': [6, 48],   # 总数量6，总金额48
#     '香蕉': [5, 25],   # 总数量5，总金额25
#     '橙子': [4, 24],   # 总数量4，总金额24
#     '葡萄': [1, 12]    # 总数量1，总金额12
# }
---

## 第8题：多层嵌套字典操作

**已知数据**：
```python
school = {
    '高一': {
        '1班': {'班主任': '张老师', '人数': 45, '教室': 'A101'},
        '2班': {'班主任': '李老师', '人数': 48, '教室': 'A102'},
        '3班': {'班主任': '王老师', '人数': 46, '教室': 'A103'}
    },
    '高二': {
        '1班': {'班主任': '赵老师', '人数': 42, '教室': 'B201'},
        '2班': {'班主任': '孙老师', '人数': 44, '教室': 'B202'}
    },
    '高三': {
        '1班': {'班主任': '周老师', '人数': 40, '教室': 'C301'},
        '2班': {'班主任': '吴老师', '人数': 38, '教室': 'C302'},
        '3班': {'班主任': '郑老师', '人数': 41, '教室': 'C303'}
    }
}
```

**任务说明**：实现以下操作函数：

1. `get_class_info(grade, class_name)`：获取某班级的所有信息
2. `get_teacher_classes(teacher_name)`：获取某老师所带的班级列表
3. `calculate_total_students()`：计算全校总学生人数
4. `find_classroom(classroom)`：根据教室号查找是哪个班级
5. `get_grade_statistics(grade)`：获取某年级的班级数、总人数、班主任列表
6. `add_class(grade, class_name, teacher, students, classroom)`：添加新班级
7. `move_classroom(grade, class_name, new_classroom)`：调整班级教室

**要求**：所有操作都要处理键不存在的情况，返回合适的信息或None

**预期结果**：每个函数返回对应的查询结果或统计信息

# 测试函数
# {'班主任': '张老师', '人数': 45, '教室': 'A101'}
# ['高一1班']
# 344
# '高三2班'
# {'班级数': 2, '总人数': 86, '班主任': ['赵老师', '孙老师']}

---

## 第9题：词频分析与文本统计

**已知数据**：
```python
article = """The quick brown fox jumps over the lazy dog. The dog sleeps while the fox runs. 
The fox is quick and brown. The dog is lazy and sleeps all day. Quick brown foxes jump over lazy dogs.
"""
```

**任务说明**：实现以下文本分析函数：

1. `word_frequency(text, case_sensitive=False)`：统计单词频率，可选择是否区分大小写
2. `filter_words_by_length(text, min_len, max_len)`：筛选出长度在指定范围内的单词（去重）
3. `get_common_words(text, n, case_sensitive=False)`：获取出现频率最高的前n个单词
4. `get_sentence_stats(text)`：统计句子总数、平均句子长度（单词数）
5. `get_word_position_map(text)`：创建每个单词到其出现位置的列表的映射（从0开始）
6. `find_anagrams(text)`：找出所有字母组成相同但顺序不同的单词对

**要求**：正确处理标点符号，返回适当的数据结构

**预期结果**：每个函数返回对应的统计结果或映射关系
# 测试函数
# 输出示例: {'the': 6, 'quick': 2, 'brown': 2, 'fox': 2, ...}
# 输出示例: ['the', 'fox', 'dog', 'over', 'lazy', 'runs', 'and', 'day', 'jump']
# 输出示例: [('the', 6), ('fox', 3), ('dog', 3), ('and', 2), ('quick', 2)]
# 输出示例: {'句子总数': 5, '平均句子长度': 7.2}
# 输出示例: {'a': [0, 3], 'cat': [1], 'and': [2], 'dog': [4]}
# 输出示例: {'eilnst': ['listen', 'silent', 'enlist']}



---

## 第10题：图书管理系统

**已知数据**：
```python
library = {
    '文学': [
        {'id': 'B001', 'title': '活着', 'author': '余华', 'year': 1993, 'available': True},
        {'id': 'B002', 'title': '百年孤独', 'author': '马尔克斯', 'year': 1967, 'available': True},
        {'id': 'B003', 'title': '围城', 'author': '钱钟书', 'year': 1947, 'available': False},
        {'id': 'B004', 'title': '平凡的世界', 'author': '路遥', 'year': 1986, 'available': True}
    ],
    '科技': [
        {'id': 'T001', 'title': 'Python编程', 'author': 'Eric', 'year': 2015, 'available': True},
        {'id': 'T002', 'title': '人工智能', 'author': '李开复', 'year': 2018, 'available': False},
        {'id': 'T003', 'title': '算法导论', 'author': 'CLRS', 'year': 2009, 'available': True}
    ],
    '历史': [
        {'id': 'H001', 'title': '史记', 'author': '司马迁', 'year': -91, 'available': True},
        {'id': 'H002', 'title': '人类简史', 'author': '赫拉利', 'year': 2011, 'available': True},
        {'id': 'H003', 'title': '明朝那些事', 'author': '当年明月', 'year': 2006, 'available': False}
    ]
}
```

**任务说明**：实现一个完整的图书管理系统，包含以下功能：

1. `search_book(keyword, field='title')`：按标题、作者或ID搜索图书
2. `get_books_by_category(category)`：获取某类别下的所有图书
3. `get_available_books(category=None)`：获取可借阅的图书（可指定类别）
4. `borrow_book(book_id, user_id)`：借书（修改available状态，记录借阅信息）
5. `return_book(book_id)`：还书
6. `get_author_books(author)`：获取某作者的所有著作
7. `get_books_by_year_range(start_year, end_year)`：获取某年份范围内的图书
8. `get_category_statistics()`：统计每个类别的图书数量、可借数量、平均年份
9. `get_most_prolific_authors(n)`：获取作品数量最多的前n位作者
10. `generate_library_report()`：生成图书馆完整报告（总藏书、借出数量、各分类占比）

**要求**：借书时需要记录借阅信息（可创建一个borrowing_history字典），所有操作要处理数据不存在的情况

**预期结果**：每个函数返回对应的查询结果或统计信息

## 第10题预期结果

### 1. `search_book(keyword, field='title')` 预期结果

```python
# 测试：search_book('python', 'title')
预期结果：
[
    {
        'id': 'T001', 
        'title': 'Python编程', 
        'author': 'Eric', 
        'year': 2015, 
        'available': True,
        'category': '科技'
    }
]

# 测试：search_book('余华', 'author')
预期结果：
[
    {
        'id': 'B001', 
        'title': '活着', 
        'author': '余华', 
        'year': 1993, 
        'available': True,
        'category': '文学'
    }
]

# 测试：search_book('B002', 'id')
预期结果：
[
    {
        'id': 'B002', 
        'title': '百年孤独', 
        'author': '马尔克斯', 
        'year': 1967, 
        'available': True,
        'category': '文学'
    }
]

# 测试：search_book('不存在的书', 'title')
预期结果：[]
```

### 2. `get_books_by_category(category)` 预期结果

```python
# 测试：get_books_by_category('文学')
预期结果：
[
    {'id': 'B001', 'title': '活着', 'author': '余华', 'year': 1993, 'available': True},
    {'id': 'B002', 'title': '百年孤独', 'author': '马尔克斯', 'year': 1967, 'available': True},
    {'id': 'B003', 'title': '围城', 'author': '钱钟书', 'year': 1947, 'available': False},
    {'id': 'B004', 'title': '平凡的世界', 'author': '路遥', 'year': 1986, 'available': True}
]

# 测试：get_books_by_category('不存在的类别')
预期结果：[]
```

### 3. `get_available_books(category=None)` 预期结果

```python
# 测试：get_available_books()  # 所有类别
预期结果：
[
    {'id': 'B001', 'title': '活着', 'author': '余华', 'year': 1993, 'available': True, 'category': '文学'},
    {'id': 'B002', 'title': '百年孤独', 'author': '马尔克斯', 'year': 1967, 'available': True, 'category': '文学'},
    {'id': 'B004', 'title': '平凡的世界', 'author': '路遥', 'year': 1986, 'available': True, 'category': '文学'},
    {'id': 'T001', 'title': 'Python编程', 'author': 'Eric', 'year': 2015, 'available': True, 'category': '科技'},
    {'id': 'T003', 'title': '算法导论', 'author': 'CLRS', 'year': 2009, 'available': True, 'category': '科技'},
    {'id': 'H001', 'title': '史记', 'author': '司马迁', 'year': -91, 'available': True, 'category': '历史'},
    {'id': 'H002', 'title': '人类简史', 'author': '赫拉利', 'year': 2011, 'available': True, 'category': '历史'}
]

# 测试：get_available_books('文学')
预期结果：
[
    {'id': 'B001', 'title': '活着', 'author': '余华', 'year': 1993, 'available': True, 'category': '文学'},
    {'id': 'B002', 'title': '百年孤独', 'author': '马尔克斯', 'year': 1967, 'available': True, 'category': '文学'},
    {'id': 'B004', 'title': '平凡的世界', 'author': '路遥', 'year': 1986, 'available': True, 'category': '文学'}
]
```

### 4. `borrow_book(book_id, user_id)` 预期结果

```python
# 测试：borrow_book('B001', 'user123')
预期结果：(True, "成功借阅《活着》")
# 同时 B001 的 available 变为 False
# borrowing_history 更新为：
{
    'user123': [
        {'book_id': 'B001', 'title': '活着', 'borrow_date': '2024-01-15', 'return_date': None}
    ]
}

# 测试：再次借阅同一本书
预期结果：(False, "图书已借出")

# 测试：borrow_book('不存在的ID', 'user123')
预期结果：(False, "图书不存在")
```

### 5. `return_book(book_id)` 预期结果

```python
# 测试：return_book('B001')
预期结果：(True, "成功归还《活着》")
# 同时 B001 的 available 变为 True
# borrowing_history 更新为：
{
    'user123': [
        {'book_id': 'B001', 'title': '活着', 'borrow_date': '2024-01-15', 'return_date': '2024-01-20'}
    ]
}

# 测试：return_book('B001')  # 已归还的书
预期结果：(False, "图书未被借出")

# 测试：return_book('不存在的ID')
预期结果：(False, "图书不存在")
```

### 6. `get_author_books(author)` 预期结果

```python
# 测试：get_author_books('余华')
预期结果：
[
    {'id': 'B001', 'title': '活着', 'author': '余华', 'year': 1993, 'available': True, 'category': '文学'}
]

# 测试：get_author_books('鲁迅')  # 不存在的作者
预期结果：[]
```

### 7. `get_books_by_year_range(start_year, end_year)` 预期结果

```python
# 测试：get_books_by_year_range(2000, 2020)
预期结果：
[
    {'id': 'T001', 'title': 'Python编程', 'author': 'Eric', 'year': 2015, 'available': True, 'category': '科技'},
    {'id': 'T002', 'title': '人工智能', 'author': '李开复', 'year': 2018, 'available': False, 'category': '科技'},
    {'id': 'H002', 'title': '人类简史', 'author': '赫拉利', 'year': 2011, 'available': True, 'category': '历史'},
    {'id': 'H003', 'title': '明朝那些事', 'author': '当年明月', 'year': 2006, 'available': False, 'category': '历史'}
]

# 测试：get_books_by_year_range(1940, 1950)
预期结果：
[
    {'id': 'B003', 'title': '围城', 'author': '钱钟书', 'year': 1947, 'available': False, 'category': '文学'}
]

# 测试：get_books_by_year_range(3000, 4000)  # 没有图书的年份范围
预期结果：[]
```

### 8. `get_category_statistics()` 预期结果

```python
预期结果：
{
    '文学': {
        '总藏书': 4,
        '可借数量': 3,  # B003 不可借
        '借出数量': 1,
        '平均年份': 1483.3  # (1993+1967+1947+1986)/4 ≈ 1483.3（注意史记是-91年，影响了平均）
    },
    '科技': {
        '总藏书': 3,
        '可借数量': 2,  # T002 不可借
        '借出数量': 1,
        '平均年份': 2014.0  # (2015+2018+2009)/3 ≈ 2014
    },
    '历史': {
        '总藏书': 3,
        '可借数量': 2,  # H003 不可借
        '借出数量': 1,
        '平均年份': 642.0  # (-91+2011+2006)/3 ≈ 642
    }
}
```

### 9. `get_most_prolific_authors(n)` 预期结果

```python
# 测试：get_most_prolific_authors(3)
预期结果：
[
    ('余华', 1),
    ('马尔克斯', 1),
    ('钱钟书', 1)
]  # 每位作者都只有1本书，所以返回前3位（按字母顺序或任意顺序）

# 如果添加了多本书的作者，例如'刘慈欣'有3本书，则：
预期结果可能为：
[
    ('刘慈欣', 3),
    ('余华', 1),
    ('马尔克斯', 1)
]
```

### 10. `generate_library_report()` 预期结果

```python
预期结果：
{
    '总藏书': 10,
    '可借数量': 7,
    '借出数量': 3,
    '借出率': '30.0%',
    '分类统计': {
        '文学': {'总藏书': 4, '可借数量': 3, '借出数量': 1, '平均年份': 1483.3},
        '科技': {'总藏书': 3, '可借数量': 2, '借出数量': 1, '平均年份': 2014.0},
        '历史': {'总藏书': 3, '可借数量': 2, '借出数量': 1, '平均年份': 642.0}
    },
    '分类占比': {
        '文学': 40.0,  # 4/10*100
        '科技': 30.0,  # 3/10*100
        '历史': 30.0   # 3/10*100
    },
    '最多产作者': [('余华', 1), ('马尔克斯', 1), ('钱钟书', 1)],
    '最新图书': ['Python编程 (2015)', '人类简史 (2011)', '算法导论 (2009)'],
    '活跃借阅用户': 1  # 假设只有user123借过书
}

# 注意：实际结果中的借阅用户数取决于borrow_book被调用的次数
# 最新图书的排序可能略有不同
```

---

## 答案

### 第1题答案
```python
numbers = [2, 4, 6, 8, 10, 12]
cube_dict = {num: num**3 for num in numbers}
# 结果: {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000, 12: 1728}
```

### 第2题答案
```python
text = "hello world python programming"

# if-else方法
count1 = {}
for c in text:
    if c != ' ':
        if c in count1:
            count1[c] += 1
        else:
            count1[c] = 1

# get方法
count2 = {}
for c in text:
    if c != ' ':
        count2[c] = count2.get(c, 0) + 1

# 结果示例: {'h': 2, 'e': 2, 'l': 4, 'o': 4, 'w': 1, 'r': 3, 'd': 2, 
#           'p': 2, 'y': 1, 't': 2, 'n': 3, 'g': 2, 'm': 2, 'a': 1, 'i': 1}
```

### 第3题答案
```python
cities = ["北京", "上海", "广州", "深圳", "杭州"]
populations = [2189, 2487, 1867, 1756, 1193]

# 方法A：zip + dict
dict1 = dict(zip(cities, populations))

# 方法B：字典推导式
dict2 = {cities[i]: populations[i] for i in range(len(cities))}

# 方法C：for循环
dict3 = {}
for i in range(len(cities)):
    dict3[cities[i]] = populations[i]

# 结果: {'北京': 2189, '上海': 2487, '广州': 1867, '深圳': 1756, '杭州': 1193}
```

### 第4题答案
```python
original = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 
            'black': '#000000', 'white': '#FFFFFF'}

reversed_dict = {code: color for color, code in original.items()}
# 结果: {'#FF0000': 'red', '#00FF00': 'green', '#0000FF': 'blue', 
#       '#000000': 'black', '#FFFFFF': 'white'}
```

### 第5题答案
```python
scores = {
    '语文': 85, '数学': 92, '英语': 78, '物理': 88, '化学': 65,
    '生物': 72, '历史': 58, '地理': 63, '政治': 71, '体育': 95
}

filtered = {subject: score for subject, score in scores.items() 
            if 60 <= score <= 90}
# 结果: {'语文': 85, '英语': 78, '物理': 88, '化学': 65, 
#       '生物': 72, '地理': 63, '政治': 71}
```

### 第6题答案
```python
ages = [5, 12, 17, 23, 31, 45, 52, 68, 71, 84, 3, 15, 27, 33, 49, 55, 62, 77, 93]

age_groups = {
    '未成年': [],
    '青年': [],
    '中年': [],
    '老年': []
}

for age in ages:
    if age <= 18:
        age_groups['未成年'].append(age)
    elif age <= 35:
        age_groups['青年'].append(age)
    elif age <= 55:
        age_groups['中年'].append(age)
    else:
        age_groups['老年'].append(age)

# 结果: {'未成年': [5, 12, 17, 3, 15], '青年': [23, 31, 27, 33], 
#       '中年': [45, 52, 49, 55], '老年': [68, 71, 84, 62, 77, 93]}
```

### 第7题答案
```python
orders = [
    {'商品': '苹果', '价格': 8, '数量': 3},
    {'商品': '香蕉', '价格': 5, '数量': 2},
    {'商品': '苹果', '价格': 8, '数量': 1},
    {'商品': '橙子', '价格': 6, '数量': 4},
    {'