# -----------------------------------------------List-------------------------------------------------------
"""
List :
1. Consecutive collection of items
2. Represent group of items as single identity, order is very important
3. Duplicate values allowed
4. Order of list is preserved
5. List is mutable
4. Represented by []
5. values separated by ,
"""
a = []  # empty list
b = [1, 2, 3, 'asdf', "Keshav", "Keshav", True, 34.65, 3 + 4j]
print(type(b))
print(b)

# order of list preserved
print(b[4])

# duplicate values
print(b[4])
print(b[5])

# list is mutable
b.append("corry Anderson")
print(b)

emp = ["Keshav", 102, "India"]
dep1 = ["IT", 10]
dep2 = ["Electronics", 2]

print(f"Name is {emp[0]} and department id is {emp[1]} and country is {emp[2]}")

# list slicing
c = [0, 1, 2, 3, 4, 5, 6, 7]
print(c[0:])
print(c[:])
print(c[2:4])
print(c[:4])

# Updating list values
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d[3] = 11
print(d)
d[1:4] = ["Rahul", "Cory", 12]
print(d)

# deleting any value form list :
del d[0]
print(d)

# sorting list values
z = ['c', 'f', 'a', 'e', 'd', 'b']
z.sort()
print(z)
# print(sorted(z))

# reverse sort
z.sort(reverse=True)
print(z)

# -------------------------------------List Operations---------------------------------------------------
"""
1. repetition
2. concatenation
3. membership
4. iteration
5. length
"""
print("---------------------------------------------------------------------------------------------")
l1 = [1, 2, 3, "Keshav", True]
print(l1 * 2)  # same items in list repeated
l1 = l1 * 2

l2 = [5, 6, 7, "cory", False]
print(l1 + l2)

print("Keshav" in l1)
print("Keshav" not in l2)

# iterations
for i in l1:
    print(i)

print(len(l1))

l3 = [1, 2, 3, 4, 5, 6]
print(max(l3))
print(min(l3))

string = "Keshav"
print(list(string))

# coping list :
original_list = [1, 2, 3, 4]
new_list = original_list[:]

original_list = [1, 2, 3, 4]
new1_list = list(original_list)

print("------------------list operations----------------------------------------------------------------")

lst = [10, 42, 73, 24, 5, 36, 23, 81, 23, 23, 101]
print(lst.count(23))
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
lst.append(2001)
print(lst)
lst.insert(5, 200)
print(lst)
lst.remove(23)
print(lst)
print(list(set(lst)))


