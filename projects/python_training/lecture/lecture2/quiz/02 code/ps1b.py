←
←
yearly_salary      = input("Your yearly salary($): ")
portion_saved      = input("The portion of your yearly salary to save(the max is 1): ")
cost_of_dream_home = input("The cost of your dream home($): ")
semi_annual_raise  = input("The portion of your yearly salary raised(the max is 1): ")

portion_down_payment = 0.25   # (25% of total home cost)
amount_saved         = 0      # (starts at $0)
r                    = 0.05   #  (5% annual rate of return)

data = [yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise]
text = ["Your yearly salary($): ", "The portion of your yearly salary to save(the max is 1): ", "The cost of your dream home($): ", "The portion of your yearly salary raised(the max is 1): " ]
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
semi_annual_raise = abs(float(data[3]))

while portion_saved > 1 or semi_annual_raise > 1:
    if portion_saved > 1:
        portion_saved = float(input("The portion should not bigger than 1: "))
    elif semi_annual_raise > 1:
        semi_annual_raise = float(input("The portion should not bigger than 1: "))

if yearly_salary == 0 or portion_saved == 0 and cost_of_dream_home != 0:
    months = float('inf')   # Python 表示无穷大的正确方式
    print("Number of months:", months)


months = 1 # ❌ months = 0 (按照下列公司可以得知，其实在第一次循环的时候，就已经过了一个月了)
while amount_saved <= cost_of_dream_home*portion_down_payment:
    # 关键是如何判断 7，14=7*2， 28=7*2*2， 56=7*2*2*2
    """
    为什么不能是是7呢?因为在if 语句的时候, 这时候months = 5, 不是6!
    所以碰到这类的时候，最好就是要想一下此刻其他的变量是什么？以及画一下时间戳。
    """
    if months % 6 != 0: # if months % 7 != 0: 
        months = months + 1 
        amount_saved += (yearly_salary / 12) * portion_saved # 上个月
        amount_saved += amount_saved * (r / 12)
    else:
        yearly_salary = yearly_salary + yearly_salary*semi_annual_raise
        months = months + 1
        amount_saved += (yearly_salary / 12) * portion_saved
        amount_saved += amount_saved * (r / 12)



print("Number of months:", months)

