←
←
## 一、Python 所有语句

- **赋值语句**（Assignment）→ 把一个值存进变量
  - 使用场景：储存数据，供后续使用
  - 例子：`name = "Tom"`

- **条件语句**（if / elif / else）→ 根据条件决定执行哪段代码
  - 使用场景：程序需要做判断和分支的时候
  - 例子：
    ```python
    if age >= 18:
        print("成年")
    else:
        print("未成年")
    ```

- **循环语句 for**（for loop）→ 按顺序遍历一个可迭代对象
  - 使用场景：需要对一组数据逐个处理
  - 例子：
    ```python
    for fruit in ["apple", "banana"]:
        print(fruit)
    ```

- **循环语句 while**（while loop）→ 满足条件就一直循环
  - 使用场景：不知道循环几次，只知道什么时候停
  - 例子：
    ```python
    while count < 5:
        count += 1
    ```

- **break** → 立刻退出当前循环
  - 使用场景：找到目标后不需要继续循环
  - 例子：
    ```python
    for n in [1, 2, 3, 4, 5]:
        if n == 3:
            break   # 找到 3 就停
    ```

- **continue** → 跳过本次循环，继续下一次
  - 使用场景：某些情况下不需要处理，直接跳过
  - 例子：
    ```python
    for n in [1, 2, 3, 4, 5]:
        if n == 3:
            continue   # 跳过 3，继续
    ```

- **pass** → 什么都不做，占位用
  - 使用场景：代码结构还没写好，先占个位置让程序不报错
  - 例子：
    ```python
    if age >= 18:
        pass   # 以后再写
    ```

- **def**（函数定义）→ 定义一段可以重复使用的代码块
  - 使用场景：某段逻辑需要多次使用，封装成函数
  - 例子：
    ```python
    def greet(name):
        print("Hello " + name)
    ```

- **return** → 从函数里返回一个值
  - 使用场景：函数计算完结果后，把结果交出去
  - 例子：
    ```python
    def add(a, b):
        return a + b
    ```

- **class**（类定义）→ 定义一个对象的模板
  - 使用场景：需要创建有属性和方法的自定义对象
  - 例子：
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name
    ```

- **import** → 引入外部模块
  - 使用场景：需要使用 Python 内置或第三方的功能
  - 例子：`import math`

- **from ... import** → 从模块里只引入某个具体的东西
  - 使用场景：只需要模块里的某一个功能，不想全部引入
  - 例子：`from math import sqrt`

- **try / except** → 捕获错误，防止程序崩溃
  - 使用场景：执行可能出错的代码，出错时做相应处理
  - 例子：
    ```python
    try:
        x = int(input())
    except ValueError:
        print("输入的不是数字")
    ```

- **raise** → 主动抛出一个错误
  - 使用场景：检测到不合法的情况，主动告知调用者
  - 例子：
    ```python
    if age < 0:
        raise ValueError("年龄不能为负数")
    ```

- **with** → 自动管理资源的开启和关闭
  - 使用场景：读写文件，用完后自动关闭，不需要手动 close
  - 例子：
    ```python
    with open("file.txt") as f:
        content = f.read()
    ```

- **del** → 删除一个变量或数据
  - 使用场景：不再需要某个变量或列表里的某个元素
  - 例子：
    ```python
    del name        # 删除变量
    del nums[0]     # 删除列表第一个元素
    ```

- **assert** → 断言某个条件必须为真，否则报错
  - 使用场景：调试时检查某个值是否符合预期
  - 例子：
    ```python
    assert age >= 0, "年龄不能为负数"
    ```

- **global** → 声明在函数内部使用全局变量
  - 使用场景：函数内部需要修改函数外部定义的变量
  - 例子：
    ```python
    count = 0
    def add():
        global count
        count += 1
    ```

- **nonlocal** → 声明在嵌套函数内部使用外层函数的变量
  - 使用场景：嵌套函数需要修改外层函数的变量
  - 例子：
    ```python
    def outer():
        x = 0
        def inner():
            nonlocal x
            x += 1
    ```

- **yield** → 让函数变成生成器，每次只返回一个值
  - 使用场景：数据量很大时，不一次性全部生成，节省内存
  - 例子：
    ```python
    def count_up(n):
        for i in range(n):
            yield i
    ```