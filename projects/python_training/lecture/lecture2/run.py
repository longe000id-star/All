←
←

# x = int(input('What x to find the cube root of? '))
# g = float(input('What guess to start with? '))
# print('Current estimate cubed = ', g**3)
# next_g = g - ((g**3 - x)/(3*g**2))
# print('Next guess to try = ', next_g)

# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x,"is the same as",y)
#     print("These are equal!")

# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("therefore, x / y is", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")
    # print("thanks!")


# What does this code print with
# y = 2
# y = 20
# y = 11
# # What if if x <= y: becomes elif x <= y: ?
# answer = ''
# x = 11
# if x == y:
#     answer = answer + 'M'
# if x <= y:
#     answer = answer + 'i'
# else:
#     answer = answer + 'T'
# print(answer)

"""
Write a program that
1. Saves a secret number.
2. Asks the user for a number guess.
3. Prints whether the guess is too low, too high, or the same as the secret.

"""
# secret_number = 10

# guess_number = float(input('Guess a number: '))
# if guess_number == secret_number:
#     print("The number is the same as the secret one")
# elif guess_number > secret_number:
#     print("The number is too high.")
# else:
    # print("The number is too low.")

initial_deposit = input("Your initial_deposit($): ")
down_payment = 200000.0
months = 36

while True:
    try:
        float(initial_deposit)
        break
    except ValueError:
        initial_deposit = input("Your initial_deposit($): ")

initial_deposit = abs(float(initial_deposit))

if initial_deposit >= down_payment - 100:
    r = 0.0
else:
    r_min = 0.0
    r_max = 1.0
    epsilon = 1e-7
    r = None

    while True:
        r_mid = (r_min + r_max) / 2
        amount_saved = initial_deposit * (1 + r_mid/12) ** months

        if abs(amount_saved - down_payment) < 100:  # 找到答案
            r = r_mid
            break
        elif amount_saved < down_payment:           # 存少了，增大r
            r_min = r_mid
        else:                                       # 存多了，减小r
            r_max = r_mid

        if r_max - r_min < epsilon:                 # 无解
            r = None
            break

print(r)
