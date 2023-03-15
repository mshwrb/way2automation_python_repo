# DATA TYPES in python
"""
Numeric - int, float, complex
Text - str
boolean - bool(true/false)
Sequence - list, tuple, range
Map - dict
Set - set and frozenset
Binary - bytes, byte_array, memory_view
type()
isinstance()
"""

x = 10.34
y = 12
z = 4j
e = "Keshav Sharma"
f = True

# double multiply means raise to the power 2^10
print(2 ** 10)

#  list[]
g = ["one", "two", "three"]

#  tuple()
h = ("one", "two", "three")

#  set{}
i = {"one", "two", "three", "three"}
si = set(["one", "two", "three", "three"])
print(si, i)

#  frozenset({})
j = frozenset({"one", "two", "three"})

# dictionary{key:value}
k = {"firstname": "keshav", "lastname": "sharma"}

# printing random numbers
import random

print(random.randrange(1, 50))

print(10 > 5)

# float value only prints upto 15 digits after decimal
a = 3.11111111111111111118
print(a)

from math import pi

print(pi)

# division always get floating number
print(100 / 100)

# without decimal
print(100 // 100)

# modulus
print(11 % 3)
