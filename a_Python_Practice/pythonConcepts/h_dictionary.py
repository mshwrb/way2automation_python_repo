# -----------------------------------------Dictionary-------------------------------------------------------
"""
Dictionary :
1. Key value pair
2. a. Key   -> Numbers,String,Tuple
   b. Value -> Python object
"""

D1 = {
    1: "24dsdsf",
    "F.Name": "Keshav",
    "L.Name": "Sharma",
    "Age": 31
}
print(type(D1))
print(D1[1])
print("-------------------------------------------------")
D2 = {
    "F.Name": "Keshav",
    "L.Name": "Sharma",
    "Age": 31,
    "IsMarried": False,
    "Salary": 1000000000.10
}

print("Name: {}".format(D2["F.Name"]))
print("L.Name: {}".format(D2["L.Name"]))
print("Age: {}".format(D2["Age"]))
print("IsMarried: {}".format(D2["IsMarried"]))
print("Salary: {}".format(D2["Salary"]))
print("-------------------------------------------------")
# update key values in a dictionary
# D2["F.Name"] = input("enter F.Name ")
# D2["L.Name"] = input("enter L.Name ")
# D2["Age"] = int(input("enter Age "))
# D2["IsMarried"] = bool(input("enter Marriage status "))
# D2["Salary"] = float(input("enter salary "))

print(D2)
print("-------------------------------------------------")
del D2["F.Name"]
print(D2)
print("-------------------------------------------------")
# iteration dictionary

# printing all key values
for a in D2:
    print(a)
print("-------------------------------------------------")
for n in D2:
    print(D2[n])

print("---------------------------------------------------------")
for c in D2.values():
    print(c)

print("----------------------------------------------------------")
for s in D2.items():
    print(s)
# printing all values in form of tuple

items = {
    "fruits": ["Apples", "Banana", "Grapes", "Mango"],
    "Price": 100,
    "Size": 12.8
}

print(items["fruits"][1])

# nested dictionary

items1 = {
    "location": "India",
    "fruits": {"Name": "Apple", "Price": 100}
}

print(items1["fruits"]["Name"])
print(items1.get("fruits").get("Price"))
print(len(items1))
print(items1.keys())
print(items1.values())

# copy of dict
original_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = original_dict.copy()

original_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = dict(original_dict)

print("--------------------------------------------------------------------------------------")
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 6, 6, 6, 4, 3, 3, 3, 4]
print(len(lst))
print({n: lst.count(n) for n in lst})
