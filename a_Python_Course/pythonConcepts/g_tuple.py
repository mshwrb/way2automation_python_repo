# -----------------------------------------------Tuple-------------------------------------------------------
"""
Tuple :
1. Used to store sequence of immutable objects
2. Mostly all other operations are similar to list
"""

T1 = (1, 2, 3, 4, 5, "Keshav", 34.54, True)
print(type(T1))

# T1[2] = 20 # TypeError: 'tuple' object does not support item assignment
print(T1[0:])
print(T1[:])
print(T1[2:4])
print(T1[1:3])
print(T1[:5])

# del T1[3] , cannot delete item in tuple

"""
Tuple operations:
1. Repetition
2. Concatenation
3. Membership Operation
4. Iteration
"""

T3 = (1, "Keshav")
print(T3 * 2)

T4 = (2, "Sharma")
print(T3 + T4)

print("Keshav" in T3)
print("Keshav" not in T3)

for i in T3:
    print(i)

# coping tuple
original_tuple = (1, 2, 3, 4)
new_tuple = original_tuple[:]
print(new_tuple)

original_tuple = (1, 2, 3, 4)
new_tuple_1 = tuple(original_tuple)
print(new_tuple_1)

