# ←
# ←

# # x = int(input('What x to find the cube root of? '))
# # g = float(input('What guess to start with? '))
# # print('Current estimate cubed = ', g**3)
# # next_g = g - ((g**3 - x)/(3*g**2))
# # print('Next guess to try = ', next_g)

# # x = int(input("Enter a number for x: "))
# # y = int(input("Enter a different number for y: "))
# # if x == y:
# #     print(x,"is the same as",y)
# #     print("These are equal!")

# # x = float(input("Enter a number for x: "))
# # y = float(input("Enter a number for y: "))
# # if x == y:
# #     print("x and y are equal")
# #     if y != 0:
# #         print("therefore, x / y is", x/y)
# # elif x < y:
# #     print("x is smaller")
# # else:
# #     print("y is smaller")
#     # print("thanks!")


# # What does this code print with
# # y = 2
# # y = 20
# # y = 11
# # # What if if x <= y: becomes elif x <= y: ?
# # answer = ''
# # x = 11
# # if x == y:
# #     answer = answer + 'M'
# # if x <= y:
# #     answer = answer + 'i'
# # else:
# #     answer = answer + 'T'
# # print(answer)

# """
# Write a program that
# 1. Saves a secret number.
# 2. Asks the user for a number guess.
# 3. Prints whether the guess is too low, too high, or the same as the secret.

# """
# # secret_number = 10

# # guess_number = float(input('Guess a number: '))
# # if guess_number == secret_number:
# #     print("The number is the same as the secret one")
# # elif guess_number > secret_number:
# #     print("The number is too high.")
# # else:
#     # print("The number is too low.")

# initial_deposit = input("Your initial_deposit($): ")
# down_payment = 200000.0
# months = 36

# while True:
#     try:
#         float(initial_deposit)
#         break
#     except ValueError:
#         initial_deposit = input("Your initial_deposit($): ")

# initial_deposit = abs(float(initial_deposit))

# if initial_deposit >= down_payment - 100:
#     r = 0.0
# else:
#     r_min = 0.0
#     r_max = 1.0
#     epsilon = 1e-7
#     r = None

#     while True:
#         r_mid = (r_min + r_max) / 2
#         amount_saved = initial_deposit * (1 + r_mid/12) ** months

#         if abs(amount_saved - down_payment) < 100:  # 找到答案
#             r = r_mid
#             break
#         elif amount_saved < down_payment:           # 存少了，增大r
#             r_min = r_mid
#         else:                                       # 存多了，减小r
#             r_max = r_mid

#         if r_max - r_min < epsilon:                 # 无解
#             r = None
#             break

# print(r)
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'cm'   # Computer Modern (数学罗马字体)
plt.rcParams['font.family'] = 'serif'
# function
def f(x):
    return x**3 - 8

# derivative
def df(x):
    return 3*x**2

# x values
points = np.array([0,1,2,3,4])
y_points = f(points)

# smooth curve
x = np.linspace(-0.5,4.5,400)
y = f(x)

plt.figure(figsize=(25,11))

# main curve (thicker)
plt.plot(x,y,linewidth=2)

for x0,y0 in zip(points,y_points):

    # thin dashed projection lines
    plt.plot([x0,x0],[0,y0],'k--',linewidth=0.8)
    plt.plot([0,x0],[y0,y0],'k--',linewidth=0.8)

    # points
    if x0 == 2:
        plt.scatter(x0,y0,color="red",s=120,zorder=5)  # large red point
    else:
        plt.scatter(x0,y0,color="black",s=30,zorder=5) # small black points
        
    # skip tangent at x=0
    if x0 == 0:
        continue

    # slope
    m = df(x0)

    # x-axis intersection
    x_axis = x0 - y0/m

    # tangent segment
    if x0 < 2:
        plt.plot([x0,x_axis],[y0,0],color="blue",linewidth=0.8)
    elif x0 > 2:
        plt.plot([x0,x_axis],[y0,0],color="blue",linewidth=0.8)

plt.axhline(0)
plt.axvline(0)

plt.xlim(-1,5)
plt.ylim(-30,60)

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$y = x^3 - 8$")

ax = plt.gca()

# 隐藏外侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax = plt.gca()

# 隐藏外侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 只保留 x 轴刻度
ax.set_xticks(points)
ax.set_yticks([])

plt.show()