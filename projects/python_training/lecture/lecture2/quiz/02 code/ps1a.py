←
←
# 6.100A PSet 1: Part A
# Name:
# Time Spent:
# Collaborators:

# Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##


yearly_salary      = input("Your yearly salary($): ")
portion_saved      = input("The portion of your yearly salary to save(the max is 1): ")
cost_of_dream_home = input("The cost of your dream home($): ")

#Initialize other variables you need (if any) for your program below ##
portion_down_payment = 0.25   # (25% of total home cost)
amount_saved         = 0      # (starts at $0)
r                    = 0.05   #  (5% annual rate of return)

"""
异常分为三类： 
1. 用户输入类型错误, 即非int; 
2. 用户输入类型int正确, 但却是负数; 
3. 用户输入出现 0.

"""
# 处理第一类异常：用户输入类型错误, 即非int。

"""
以下是第一版的答案, 有错误, 也就是对float(string)返回的值不清楚,
我以为不能转换就返回False,成功转换就返回True。实际float(string)会报错。 

number_dot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.']
for str(i) in yearly_salary:
    if not i in number_dot:
            yearly_salary = input("Error, entry your yearly salary again:$ ")
            for i in yearly_salary:
                if not i in number_dot:
                    break
                else: 
                    continue
    else:
        continue

else:
    yearly_salary = float(yearly_salary)
    portion_saved = float(portion_saved)
    cost_of_dream_home = float(cost_of_dream_home)

"""

# 第二版，使用try/except, 这是处理报错的语句

"""
这里再循环的地方出错。 

input = [yearly_salary, portion_saved, cost_of_dream_home]
for i in input: ❌
    try:
        i = float(i)
    except ValueError:
        yearly_salary  = input("Your yearly salary again:$ ")
    else:
        continue

"""
# 第三版， 继续使用try/except, 但循环改成对index的循环，而非值。现在已经成功对int输入进行了验证，现在还要对变为positive. 
# 问题还需要解决的是：如何在用户不断输错的情况下，不断循环直到用户输对
data = [yearly_salary, portion_saved, cost_of_dream_home]
text = ["Your yearly salary($): ", "The portion of your yearly salary to save(the max is 1): ", "The cost of your dream home($): " ]
for i in range(len(data)):  
    while True:
        try:
            float(data[i])
            break
        except ValueError:
            data[i]  = input(f" {text[i]}:$ ")
        
yearly_salary = abs(float(data[0]))
portion_saved = abs(float(data[1]))
cost_of_dream_home = abs(float(data[2]))

# 另外还要重新思考portion_saved的值，因为这个数值 <= 1. 
# 问题还需要解决的是：如何在用户不断输错的情况下，不断循环直到用户输对
while portion_saved > 1:
        portion_saved = float(input("The portion should not bigger than 1: "))


# 现在就是处理 0 的情况下. 如果yearly_salary 或者 portion_saved 其中一个为0(前提是cost_of_dream_home不为0，那么month = ♾️。 
# 如果cost_of_dream_home为0， 那么month也是 0. 

if yearly_salary == 0 or portion_saved == 0 and cost_of_dream_home != 0:
    months = float('inf')   # Python 表示无穷大的正确方式
    print("Number of months:", months)

# 计算months
#amount_saved += (yearly_salary / 12) * portion_saved # 一个月从工资中取出存多少钱
#amount_saved += amount_saved * (r / 12) #这个是每个月从工资取出份额存钱 + 上个月的利息 

#这个理解也是错误的，因为这个是跟现值有关 ❌（因为这种方法是每月存定期，但是每个月的利息是没有再投资的）❌ months = (12*(1+r**2)*cost_of_dream_home*portion_down_payment) / (yearly_salary*portion_saved)

"""
这里的公式还是错了，因为：
你现在的公式只存一次存，复利增长。 而题目则是复利增长年金公式每月存一次，每笔都复利。
看来我对金融公司好像真的不明白啊。 
那么这时候最好不要考公式，而是逻辑。 
monthly_saving = (yearly_salary / 12) * portion_saved 
target = cost_of_dream_home * portion_down_payment

months = math.log(target / monthly_saving) / math.log(1 + r) + 1

"""

"""
# Note: investment return is calculated on amount saved at the START of each month.
amount_saved += (yearly_salary / 12) * portion_saved # 一个月从工资中取出存多少钱
amount_saved += amount_saved * (r / 12) #这个是每个月从工资取出份额存钱 + 上个月的利息 

"""
"""
yearly_salary = 1440, portion_saved = 0.1, cost_of_dream_home = 240000
portion_down_payment = 0.25, amount_saved = 0, r = 0.05
# 第一个月(也就是下个月的开始) 
amount_saved = amount_saved + (yearly_salary / 12) * portion_saved 
amount_saved = 0 + (1440/12)*0.1 = 12 #这是上个月初从工资取的钱
amount_saved = 12 + 12*(0.05/12) = 12.05 # (这是)经过一个月后我现在账户的钱

然后我正准备继续存钱 (yearly_salary / 12) * portion_saved = 12 此时账户有 12 + 12.05
# 第二个月
amount_saved += (yearly_salary / 12) * portion_saved # 上个月
amount_saved = 12.05 + 12 = 24.5 # 这是上个月存入的钱+账户已有的钱
amount_saved += amount_saved * (r / 12)
amount_saved = 24.5 + 24.5 * (0.05/12) # 这是(上个月存入的钱+账户已有的钱) 以及他们的利息。
# 目前已经过了 两个月，我总共存入了两笔钱，正好两个月，如果够买房了，我就不在这个月初存入了。
所以，此时需要判断是的 amount_saved >= cost_of_dream_home*portion_down_payment
于是就停止了。那么这里需要判断的month，以及如何让这个计算循环。 
我刚才还想是否for i in range(int('inf')) ？ 这是❌，然后满足amount
"""
months = 1 # ❌ months = 0 (按照下列公司可以得知，其实在第一次循环的时候，就已经过了一个月了)
while amount_saved <= cost_of_dream_home*portion_down_payment:
    months = months + 1 
    amount_saved += (yearly_salary / 12) * portion_saved # 上个月
    amount_saved += amount_saved * (r / 12)   

print("Number of months:", months)

# 以上可以知道，当我们没有对象可以通过一个一个取来确定循环的时候，这个时候使用while最好
# 另外我终于意识到了使用programming循环的作用了，因为判断逻辑很简单。但如果需要使用数学，那可是一个复杂的数学公式。







#Determine how many months it would take to get the down payment for your dream home below ## 


"""
================================================================
PART A — Saving for a House
================================================================

You have just graduated from MIT and have a job! You move to the
Bay Area and decide to start saving for a home. Your goal is to
find the number of months it takes to save up for a down payment.

----------------------------------------------------------------
2.1 User Inputs (cast as floats, in this order)
----------------------------------------------------------------
  yearly_salary      — the starting yearly salary
  portion_saved      — portion of salary to save (e.g. 0.1 for 10%)
  cost_of_dream_home — the cost of your dream home

----------------------------------------------------------------
2.2 Fixed Program Variables
----------------------------------------------------------------
  portion_down_payment = 0.25   (25% of total home cost)
  amount_saved         = 0      (starts at $0)
  r                    = 0.05   (5% annual rate of return)

----------------------------------------------------------------
2.3 Monthly Update Formula
----------------------------------------------------------------
  amount_saved += (yearly_salary / 12) * portion_saved
  amount_saved += amount_saved * (r / 12)

  Note: investment return is calculated on amount saved at the
  START of each month.

----------------------------------------------------------------
2.4 Output
----------------------------------------------------------------
  months = <calculated value>
  print("Number of months:", months)

----------------------------------------------------------------
2.5 Test Cases
----------------------------------------------------------------
  Case 1: salary= / saved=0.17 / cost=750000
          → Number of months: 97

  Case 2: salary=65000  / saved=0.20 / cost=400000
          → Number of months: 79

  Case 3: salary=350000 / saved=0.30 / cost=10000000
          → Number of months: 189

  Run ps1_tester.py in the same folder as ps1a.py and
  put_in_function.py. You should pass the first 3 test cases.
================================================================

"""