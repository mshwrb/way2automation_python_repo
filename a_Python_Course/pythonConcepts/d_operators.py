# ----------------------------------- Operators in python------------------------------------------------
"""
1. Arithmatic
2. Comparison/Relational
3. Equality
4. Logical
5. Bitwise
6. Shift
7. Assignment
8. Ternary
9. Membership
10. Identity
"""

# ------------------------------------ARITHMATIC OPERATORS------------------------------------------------
'''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus (%)
6. Exponential (**)
7. Floor Division (//)
'''
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# ------------------------------------COMPARISON/RELATIONAL OPERATORS--------------------------------------
'''
Greater Than (>)
Greater Than equal to (>=)
Smaller Than (<)
Smaller Than equal to (<=)
'''
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print("--------------------------------")
# comparing ascii value of strings Dog and Cat
s1 = "Cat"
s2 = "Dog"
print(s1 > s2)
print(s1 >= s2)
print(s1 < s2)
print(s1 <= s2)

# printing ascii value of variable/string
print(ord("a"))
print(ord("A"))

print('apple' > 'apple')
print('apple' >= 'apple')
print('apple' < 'apple')
print('apple' <= 'apple')

# relational operator chaining
print(60 > 50 > 40 > 30 > 20 > 10)

# -------------------------------------EQUALITY OPERATORS--------------------------------------------------
'''
Equal To (==)
Not Equal To (!=)
'''
a = 10
b = 20
print("------------------------------------------------------------------------------------------------")
print(a == b)
print(a != b)
print('------------------------------------------------------------------------------')
print(1 == True)
print(0 == True)
print(0 == False)
print(10 == 10.0)
print("way_2_automation" == "way_2_automation")

# -------------------------------------LOGICAL OPERATORS-----------------------------------------------------
'''
And --> Return true whenever both the arguments are true in nature
Or --> Return true whenever either of the arguments are true in nature 
Not --> Return reverse
'''

print("-----logical operators----------------")
'''
--------And----------------------------------------
1. If x evaluates False, then the result is value x 
2. If x evaluates True, then the result is value y
'''
print(True and True)
print(1 and 0)
print(10 and 20)
print(0 and 20)
print('-----------------OR------------------------')

print(10 or 20)
print(0 or 10)

# username = input('Enter username ')
# password = input('Enter password ')
# if username == 'way2automation' or password == 'test':
#     print('valid user')
# else:
#     print('invalid user')

print(not True)
print(not False)
print(not a == 10)
# ------------------------------------BITWISE OPERATORS-------------------------------------------------
'''
1. Bitwise And (&)
2. Bitwise Or (|)
3. Bitwise XOR (^)
4. Bitwise Compliment (~)
'''
# ------------------------------------Bitwise And (&) operators-----------------------------------------
'''
<operator> <operand> <operator>   
if both bits are 1 then the result is 1 otherwise everytime it is 0      
  |------------------|
  | A |   | B |Result|
  | 0 | & | 0 |--> 0 |
  | 0 | & | 1 |--> 0 |
  | 1 | & | 0 |--> 0 |
  | 1 | & | 1 |--> 1 |
  |------------------|
'''
print('----------bitwise &----------------------')
print('getting binary value of 16 and 18')
print(bin(16))
print(bin(18))
print(16 & 18)
'''
why 16 because :
binary 16 == 0b10000
binary 18 == 0b10010
  |------------------|
  |16 |   |18 |Result|
  | 1 | & | 1 |--> 1 |
  | 0 | & | 0 |--> 0 |
  | 0 | & | 0 |--> 0 |
  | 0 | & | 1 |--> 0 |
  | 0 | & | 0 |--> 0 |
  |------------------|
  result: 10000 == 16
'''

# ------------------------------------Bitwise Or (|) operators--------------------------------------------
'''
<operator> <operand> <operator>   
if atleast 1 operator is 1 then result is 1 otherwise 0      
  |------------------|
  | A |   | B |Result|
  | 0 | | | 0 |--> 0 |
  | 0 | | | 1 |--> 1 |
  | 1 | | | 0 |--> 1 |
  | 1 | | | 1 |--> 1 |
  |------------------|
'''
print(16 | 18)
'''
why 18 because :
binary 16 == 0b10000
binary 18 == 0b10010
  |------------------|
  |16 |   |18 |Result|
  | 1 | | | 1 |--> 1 |
  | 0 | | | 0 |--> 0 |
  | 0 | | | 0 |--> 0 |
  | 0 | | | 1 |--> 1 |
  | 0 | | | 0 |--> 0 |
  |------------------|
  result: 10010 == 18
'''
# ------------------------------------Bitwise XOR (^) operators----------------------------------------------
'''
<operator> <operand> <operator>   
if both bits are different then result is 1 otherwise 0      
  |------------------|
  | A |   | B |Result|
  | 0 | ^ | 0 |--> 0 |
  | 0 | ^ | 1 |--> 1 |
  | 1 | ^ | 0 |--> 1 |
  | 1 | ^ | 1 |--> 0 |
  |------------------|
'''
print(16 ^ 18)
print(bin(2))
'''
why 2 because :
binary 16 == 0b10000
binary 18 == 0b10010
  |------------------|
  |16 |   |18 |Result|
  | 1 | | | 1 |--> 0 |
  | 0 | | | 0 |--> 0 |
  | 0 | | | 0 |--> 0 |
  | 0 | | | 1 |--> 1 |
  | 0 | | | 0 |--> 0 |
  |------------------|
  result: 00010 == 2
'''
# ------------------------------------Bitwise Compliment (~) operator---------------------------------------
'''
-(n+1)
'''
print(~(-4))
# ------------------------------------SHIFT OPERATORS----------------------------------------------------------
"""
shifting bits left/right:

Left shift operators (<<)
Right shift operators (>>)
"""
# ------------------------------------Left shift operator------------------------------------------------------
print(10 << 2)
print(bin(10))
'''
why 40
binary 10 == 0b1010
_________________________________________________
|  0  |  0  |  0  |  0  |  1  |  0  |  1  |  0  | 
-------------------------------------------------
10 << 2 
_________________________________________________
|     |     |  0  |  0  |  1  |  0  |  1  |  0  | 
-------------------------------------------------
_________________________________________________
|  0  |  0  |  1  |  0  |  1  |  0  |     |     | 
-------------------------------------------------
_________________________________________________
|  0  |  0  |  1  |  0  |  1  |  0  |  0  |  0  | 
-------------------------------------------------
0b101000 == 40
'''
print(0b101000)
print(bin(40))
# ------------------------------------Right shift operator------------------------------------------------------
print(10 >> 2)
print(bin(10))
print(0b000010)
'''
why 2
binary 10 == 0b1010
_________________________________________________
|  0  |  0  |  0  |  0  |  1  |  0  |  1  |  0  | 
-------------------------------------------------
10 >> 2 
_________________________________________________
|  0  |  0  |  0  |  0  |  1  |  0  |     |     | 
-------------------------------------------------
_________________________________________________
|     |     |  0  |  0  |  0  |  0  |  1  |  0  | 
-------------------------------------------------
_________________________________________________
|  0  |  0  |  0  |  0  |  0  |  0  |  1  |  0  | 
-------------------------------------------------
0b000010 == 2
'''
# ------------------------------------ASSIGNMENT OPERATORS----------------------------------------------------------
'''
= , += , *= , -= etc
'''
print('------------------assignment operators--------')
x = 20
x += 10  # x = x + 10
print(x)
x *= 10  # x = x * 10
print(x)
x -= 10  # x = x - 10
print(x)

# python does not support increment and decrement operators
# print(x++)/(x--)

# ------------------------------------TERNARY OPERATORS----------------------------------------------------------
'''
It is conditional operator and there is no specific keyword for it
var = First value if condition else second value

(expression_1) if (expression_2) else (expression_3)
expression_2 == True  ----> expression_1
expression_2 == False ----> expression_3
'''
a = 10
b = 20
c = 30 if a > b else 40
print(c)

# a = int(input('enter the number a '))
# b = int(input('enter the number b '))
# minimum = a if a < b else b
# print(minimum)

# -----------------------------------MEMBERSHIP AND IDENTITY OPERATORS---------------------------------------------
'''
1. is
2. is not
3. in 
4. not in

a is not b , return true if both reference variable pointing to same object
'''
a = 10
b = 10
print(a is b)
print(a is not b)

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, "asdf"]
print(30 in a)
print(100 in a)
print(100 not in a)
print(30 not in a)
