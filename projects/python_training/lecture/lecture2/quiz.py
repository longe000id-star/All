←
←
# <!-- # - Answers and explanations are provided at the end
# # Python Strings, Input/Output, and Branching - Quiz
# # Based on Lecture 2: Strings, Input/Output, and Branching

# # Instructions:
# # - This quiz contains multiple choice questions, code reading exercises, and coding challenges
# # - Difficulty levels: Easy, Medium, Hard -->
# <!-- # - For coding challenges, write your solution in the provided space -->

# # 7/10

# # EASY QUESTIONS

# 1. MULTIPLE CHOICE - String Concatenation
# What will be the output of the following code? 
# a = 'Hello'
# b = 'World'
# c = a + ' ' + b
# d = a * 3
# print(c)
# print(d)

# A) c = 'HelloWorld', d = 'HelloHelloHello'
# B) c = 'Hello World', d = 'HelloHelloHello'
# C) c = 'Hello World', d = 'Hello Hello Hello'
# D) c = 'HelloWorld', d = 'Hello Hello Hello'

# > (B)


# 2. CODE READING - String Slicing
# What will this code output?
# s = 'Python Programming'
# print(s[0:6]) 
# print(s[7:])
# print(s[::-1])

# > 1. 'Python '
# > 2. 'Programming'
# > 3. 'gnimmargorP onhtyP'

# 3. MULTIPLE CHOICE - Input/Output
# Which of the following is the correct way to get user input and print a formatted message?

# A) name = input('Enter name'); print('Hello', name)
# B) name = input('Enter name: '); print(f'Hello {name}!')
# C) name = input('Enter name: '); print('Hello ' + name + '!')
# D) All of the above are correct

# > D

# 4. CODE READING - Basic Branching
# What will this code output when the user enters 5?
# num = int(input('Enter a number: '))
# if num > 0:
#     print('Positive')
# elif num < 0:
#     print('Negative')
# else:
#     print('Zero')

# > ‘Positive' ❌ Positive


#                    MEDIUM QUESTIONS

# 5. MULTIPLE CHOICE - String Methods
# What will be the output of this code?
# text = '  Hello World!  '
# result = text.strip().upper().replace('!', '.')
# print(result)

# A) 'HELLO WORLD.'
# B) '  HELLO WORLD!  '
# C) 'HELLO WORLD!'
# D) 'hello world.'

# > A


# 6. CODE READING - Advanced Branching
# What will this code output when the user enters 85?
# grade = float(input('Enter your grade (0-100): ')) 
# if grade >= 90:
#     letter = 'A'
# elif grade >= 80:
#     letter = 'B'
# elif grade >= 70:
#     letter = 'C'
# elif grade >= 60:
#     letter = 'D'
# else:
#     letter = 'F'
# print(f'Your letter grade is: {letter}')

# > Your letter grade is: B

# 7. MULTIPLE CHOICE - String Formatting
# Which of the following f-string expressions will produce the output 'The result is 12.35' when x = 12.34567?

# A) f'The result is {x:.2f}'
# B) f'The result is {x:2f}'
# C) f'The result is {x:.2}'
# D) f'The result is {x:2.2f}'

# > A ❌C

# 8. CODE READING - String Processing
# What will this code output?
# text = 'Hello World!'
# words = text.split()
# print(len(words))
# print(words[0])
# print(text.upper().replace('O', '0'))

# > 1. 12
# > 2. ‘Hello' ❌'H'
# > 3. ‘HELL0 W0RLD' ❌'HELL0 WORLD!'


#                     HARD QUESTIONS

# 9. MULTIPLE CHOICE - Complex String Operations
# What will be the output of this code?
# s = 'Programming'
# print(s[1:8:2])
# print(s[-1:-6:-1])
# print(s[4:])

# A) 'rgam', 'gnimm', 'ramming'
# B) 'rgam', 'gnimm', 'ramming'
# C) 'rgam', 'gnimm', 'ramming'
# D) 'rgam', 'gnimm', 'ramming'

# > 1. 'rgam'
# > 2. 'gnimm'
# > 3. 'ramming'

# 10. CODE READING - Input Validation
# What will this code do when the user enters 'abc'?
# try:
#     num = int(input('Enter a number: '))
#     print(f'You entered: {num}')
# except ValueError:
#     print('Invalid input! Please enter a valid number.')

# > 'Invalid input! Please enter a valid number.'

# 11. CODING CHALLENGE - String Analysis
# Write a function that takes a string and returns:
# - The number of vowels
# - The number of consonants
# - The string 


# 9/10

# Vowels = ['a', 'e', 'i', 'o', 'u']
# number_vowel = 0
# Consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
# number_consonant = 0
# Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# text = input('Entry a text: ')
# lower_text = text.lower()
# all_letter = []
# for i in lower_text: # ❌ for i in text: 因为这里的 text还包括大写，如果输入的 text 包括大写，那么程序就会自动跳过. 
#     if i in Alphabet:
#         all_letter.append(i)
#     else: continue
# for i in all_letter:
#     if i in Vowels:
#         number_vowel = number_vowel + 1
#     elif i in Consonants:
#         number_consonant = number_consonant + 1
#     else:
#         continue

# print(number_vowel)
# print(number_consonant)
# print(text)


# > 首先，要先处理数据，得先清洗数据，减少噪音。比如'  Hello World!  ' >>> 'helloworld'这里需要把空格和标点符号给取消。当然也可以直接处理数据。这样就不用还要判断大写。lower()

# > 思路：首先先确定AEIOU这五个元音，其他都是辅音。可以分别分析，先可以先分析完元音，然后用计算出总字母数（要求去掉符号，空格等）
# > 然后 reversed的话，也可以一个一个替换掉，但后也可以使用 s[:: -1]这个得到一个新的 string。


# 12. CODING CHALLENGE - Interactive Calculator
# Write a program that:
# - Asks the user for two numbers
# - Asks for an operation (+, -, *, /)
# - Performs the calculation
# - Handles division by zero


# 这里还有检测用户输入的数据结构，必须要为 int OR float
# first_number = float(input('Entry the first number: '))
first_number = input('Entry the first number: ') # 的确这里将永远是 str,而不是 int/float, input 后面蒋永远是 str
second_number = input('Entry the second number: ')

if type(first_number) is int or type(first_number) is float:
    first_number = float(first_number)
    
else:
    print("error, entry again: ")
    first_number = input('Entry the first number: ')
    first_number = float(first_number)

if type(second_number) is int or type(second_number) is float:
    second_number = float(second_number)
else:
    print("error, entry again: ")
    second_number = input('Entry the second number: ')
    second_number = float(second_number)


def add(first_number, second_number):
    result_add = first_number + second_number
    return result_add

def sub(first_number, second_number):
    result_sub = first_number - second_number
    return result_sub

def mul(first_number, second_number):
    result_mul = first_number * second_number
    return result_mul

def dev(first_number, second_number):
    if second_number == 0:
        second_number = float(input('Cannot be 0, entry the second number again: '))
        result_dev = first_number / second_number
        return result_dev
    else:
        result_dev = first_number / second_number
        return result_dev

print(add(first_number, second_number))
print(sub(first_number, second_number))
print(mul(first_number, second_number))
print(dev(first_number, second_number))


# # ANSWERS AND EXPLANATIONS

# 1. B
# Explanation: String concatenation with + joins strings, and * repeats strings.
# Result: c = 'Hello World', d = 'HelloHelloHello'

# 2. 
# s[0:6] = 'Python'
# s[7:] = 'Programming'
# s[::-1] = 'gnimmargorP nohtyP'
# Explanation: s[0:6] gets characters 0-5, s[7:] gets from index 7 to end, s[::-1] reverses the string.

# 3. D
# Explanation: All three methods are valid ways to get input and display output in Python.

# 4. 'Positive'
# Explanation: Since 5 > 0, the first condition is true and 'Positive' is printed.

# 5. A
# Actual result: 'HELLO WORLD.'
# Explanation: strip() removes whitespace, upper() converts to uppercase, replace() changes '!' to '.'

# 6. 'Your letter grade is: B'
# Explanation: Since 85 >= 80 but 85 < 90, the second elif condition is true.

# 7. A
# Actual result: The result is 12.35
# Explanation: .2f formats the number to 2 decimal places.

# 8. 
# len(words) = 2
# words[0] = 'Hello'
# text.upper().replace('O', '0') = 'HELL0 W0RLD!'
# Explanation: split() creates a list of words, len() counts them, upper() converts to uppercase, replace() substitutes characters.

# 9. A
# Actual results:
# s[1:8:2] = 'rgam'
# s[-1:-6:-1] = 'gnimm'
# s[4:] = 'ramming'
# Explanation: s[1:8:2] takes every 2nd character from index 1 to 7, s[-1:-6:-1] reverses characters from end, s[4:] gets substring from index 4.

# 10. 'Invalid input! Please enter a valid number.'
# Explanation: int('abc') raises a ValueError, which is caught by the except block.

# 11. 
# ```python

# def analyze_string(text: str) -> dict:
#     vowels = "aeiouAEIOU"
#     vowel_count = sum(1 for char in text if char in vowels)
#     consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
#     reversed_text = text[::-1]
    
#     return {
#         'vowels': vowel_count,
#         'consonants': consonant_count,
#         'reversed': reversed_text
#     }

# ```

# Test with 'Hello World!':
# Vowels: 3
# Consonants: 7
# Reversed: '!dlroW olleH'

# 12.
# ```python
# def interactive_calculator():
#     try:
#         num1 = float(input('Enter first number: '))
#         num2 = float(input('Enter second number: '))
#         operation = input('Enter operation (+, -, *, /): ').strip()
        
#         if operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '/':
#             if num2 == 0:
#                 print('Error: Division by zero!')
#                 return
#             result = num1 / num2
#         else:
#             print('Error: Invalid operation!')
#             return
        
#         print(f'Result: {num1} {operation} {num2} = {result}')
        
#     except ValueError:
#         print('Error: Please enter valid numbers!')
# ```
# Quiz completed! Review the solutions and practice coding.
# ============================================================
