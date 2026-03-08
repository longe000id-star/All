←
←
#Finger Exercise Lecture 14
#Question 1: Implement the function that meets the specifications below:
#
#def keys_with_value(aDict, target):
#    """
#    aDict: a dictionary
#    target: an integer or string
#    Assume that keys and values in aDict are integers or strings.
#    Returns a sorted list of the keys in aDict with the value target.
#    If aDict does not contain the value target, returns an empty list.
#    """
#    # Your code here  
#    # Examples:
#    key = list(aDict.keys())  
#    value = list(aDict.values()) 
#    index = []
#    i = 0
#    for target in value:  
#        if i >= len(value):  
#            if index is None:
#                return []
#            else:
#                key_with_value = []
#                if i >= len(index):  
#                    print (key_with_value)
#                else:
#                    key_with_value.append(str(key[index[i]]))  
#                    i = i + 1
#        else:
#            if target == value[i]:
#                index.append(i)
#                i = i + 1
#            else: 
#                i= i + 1

# MY CODE

empty_list = []
item = {}
found_key = []

def keys_with_value(aDict, target):
    if not target is None:
        if target in list(aDict.values()):
            for k,v in aDict.items():
                if v == target:
                    found_key.append(k)
                else:
                   continue # ❌return ()
            return found_key 
        else:
            return empty_list
    else:
        return empty_list

aDict = {1:2, 2:4, 5:2}
target = 2      
print(keys_with_value(aDict, target))

# DEBUG 
# quiz.py
#empty_list = []
#item = {}
#found_key = []
#def keys_with_value(aDict, target):
#    print("--- 函数开始 ---")
#    print(f"接收到的字典: {aDict}")
#    print(f"接收到的目标值: {target}")
#    print(f"当前全局 found_key 初始值: {found_key}")
#
#    if not target is None:
#        print("--> 条件1: target 不是 None")
#        if target in list(aDict.values()):
#            print(f"--> 条件2: {target} 在值列表 {list(aDict.values())} 中")
#            for k, v in aDict.items():
#                print(f"   --- 循环开始: 当前键 k={k}, 值 v={v} ---")
#                if v == target:
#                    print(f"     匹配成功！将键 {k} 加入 found_key")
#                    found_key.append(k)
#                    print(f"     当前 found_key: {found_key}")
#                else:
#                    print(f"     值 {v} 不匹配 {target}，准备执行 return ()")
#                    continue # ❌ return ()
#            print(f"--> 循环结束，准备返回 found_key: {found_key}")
#            return found_key
#        else:
#            print(f"--> 条件2不成立: {target} 不在值列表中，返回 empty_list")
#            return empty_list
#    else:
#        print("--> 条件1不成立: target 是 None，返回 empty_list")
#        return empty_list
#
#aDict = {1:2, 2:4, 5:2}
#target = 2      
#print(keys_with_value(aDict, target))
     
#我觉得再解决问题的时候：不要一来就写代码，而是先思考算法. 此外，我觉得我可能真的不知道怎么使用"for" & "if" 
#可以想到用“计算思维”（Computational Thinking）这个核心术语来回答，它包含了分解、模式识别、抽象、算法设计四个步骤，正好能解释用户遇到的情况。
#还可以引入“心智模型”和“程序执行模型”的差异，以及“冯·诺依曼架构”对计算机顺序执行的影响。
#这样既能满足用户对理论术语的需求，又能给出实用的学习建议。
#
#以下是代码中的主要错误：
#
#1. **变量名覆盖**：参数 `target` 被循环变量 `for target in value` 覆盖，导致后续无法访问原始的 `target` 值。
#2. **循环逻辑混乱**：手动维护索引 `i` 的同时又遍历 `value`，两者不同步，导致索引越界或比较错误。
#3. **索引越界处理不当**：`if i >= len(value)` 分支内试图用 `i` 访问 `index[i]`，此时 `i` 可能已超出 `index` 范围，且分支逻辑不清晰。
#4. **未返回结果**：函数没有明确的 `return` 语句，默认返回 `None`，不符合题目要求（应返回列表）。
#5. **局部变量作用域**：`key_with_value` 定义在分支内，外部无法访问，且未返回。
#6. **无排序操作**：题目要求返回排序后的列表，但代码未进行排序。
#7. **多余的类型转换**：`str(key[index[i]])` 将键强制转换为字符串，应保持原类型。
#8. **无用的打印语句**：`print(key_with_value)` 不应出现在最终代码中。
#9. **条件判断错误**：`if index is None` 永远为假，因为 `index` 初始化为空列表，不会为 `None`。
#10. **整体算法错误**：代码逻辑无法正确收集值为 `target` 的键，即使修正局部问题也无法达到目的。
#    
#    
#    
#为什么不可以呢？把key &value 分开，只要知道value是哪一合个以及index，aDict = {1:2, 2:4, 5:2}
#target = 2   
#print(keys_with_value(aDict, target)) # prints the list [1,5]
#
#比如key = [1,2,5], value=[2,4,2], target =2
#那么我们只要找出target，就是value[0], value[2],不久对应key[0],key[2]?
#    
#
#            
#
## examples:
#aDict = {1:2, 2:4, 5:2}
#target = 2   
#print(keys_with_value(aDict, target)) # prints the list [1,5]
#
#
#
#
#
#
#
#Question 2: Implement the function that meets the specifications below:
def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    # Your code here  
    empty_list = []
    found_key = []
    for k, v in d.items():
        sum = 0
        for i in v: 
            sum = sum + i
        else:
            if sum > 0:
                found_key.append(k)
                found_key.sort()
    else:
        return found_key
  
  

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]
