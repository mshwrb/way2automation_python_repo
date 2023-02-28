# ----------------------------------Python Flow Control-------------------------------------------
"""
1. if statement
2. if-else statement
3. if-elif-else statement
4. for loops
5. while loops
6. nested loops
7. break statement
8. continue statement
9. loops with else block
10. pass statement
"""

# ----------------------------------------if statement---------------------------------------------------
a = 10
b = 30
if a > b:
    print('a is greater than b')
else:
    print('b is greater than a')

# marks = int(input('Enter the marks '))
# section = input('Enter section ')
# if 90 < marks <= 100:
#     if section == 'A':
#         print('Brilliant class')
#     grade = 'A+'
#     print(grade)
# elif 80 <= marks < 90:
#     grade = 'A'
#     print(grade)
# elif 70 <= marks < 80:
#     grade = 'B'
#     print(grade)
# else:
#     grade = 'Average'
#     print(grade)
# ----------------------------------------loops------------------------------------------------------
'''
1. for loop
2. while loop
(Note: no do while loops)
(used on sequences: range,tuple,list,dictionary)
'''
# ----------------------------------------For loop------------------------------------------------------
sequence = "Keshav"
i = 0
for x in sequence:
    print(f"The character present is {x} and the index is {sequence.index(x)}")
    i += 1
print('--------------------------------------')
for x in range(10):  # 0-(n-1)
    print("way2automation ", x)
print('--------------------------------------')
for x in range(1, 11):
    print(x)
print('--------------------------------------')
for x in range(1, 30, 3):
    print(x)
print('--------------------------------------')
# n = int(input('enter the number: '))
# for x in range(1, 11):
#     print(n, " * ", x, " = ", n * x)
print('--------------------------------------')
# eval() --> accept any form of data like tuple,list etc
# List = eval(input('Enter the numbers for addition: '))
# sum = 0
# for x in List:
#     sum += x
# print("Total sum is: ", sum)
print('--------------------------------------')
a = 2
for x in range(1, 30, a):
    a += 2
    print(x)
print('--------------------------------------')
string = "My Name is Keshav Sharma"
s = string.split(" ")
for x in s:
    print(x)
# ----------------------------------------While loop------------------------------------------------------
i = 0
while i < 10:
    print(i)
    i += 1
# Print sum of first n numbers
# n = int(input("Enter the number "))
# sum = 0
# while n >= 1:
#     sum += n
#     n -= 1
# print(f"total sum: {sum}")
# ------------------------------------Break statement----------------------------------------------------
print('-----------------------break statement-----------------------')
for i in range(10):
    print(i)
    if i == 7:
        break
# ------------------------------------Continue statement----------------------------------------------------
print('-------------------continue statement---------------------------')
for x in range(10):
    if x % 2 == 0:
        print('even number: ', x)
        continue
    print('odd numbers are: ', x)
print('-------------------continue statement-----2----------------------')
for x in range(10):
    if x == 7:
        print(x)
        break
    elif x == 5:
        continue
    print(x)
# -------------------------------loop with else block-------------------------------------------------------
"""
The else block only executes when for loop successfully executed
"""
print("-----------------------loop with else block------------------------------")
cart = [10, 20, 3000, 40, 50, 600, 70, 80, 90, 100]
for item in cart:
    if item > 500:
        print("this item is not allowed")
        continue  # break/continue
    print(item)
else:
    print("all items are successfully processed")
# -------------------------------------Pass statement----------------------------------------------------
print("--------------pass statement----------------------------")
for x in "Keshav":
    pass

# list inliner
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [n for n in a if n % 2 == 0]
print(type(x))
print(x)

print("--------------------------------------------------------------------------------")

# set inliner
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
x = {n for n in a if n % 2 == 0}
print(type(x))
print(x)

print("--------------------------------------------------------------------------------")

# tupple inliner
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
x = [n for n in a if n % 2 == 0]
print(type(x))
print(x)

print("--------------------------------------------------------------------------------")

# dict inliner
a = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
x1 = {n: n for n in a.values() if n % 2 == 0}
print(type(x1))
print(x1.values())
print(x1.keys())

