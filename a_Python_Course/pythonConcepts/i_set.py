# -----------------------------------------Sets---------------------------------------------------------------
"""
Sets :
1. Similar to List
2. It can store different types of values Int,String,Float,Bool etc.
3. Set cannot have duplicate values
4. Set are defined using {} , collection which is un_indexed and unordered
"""

s1 = {"Selenium", "Appium", "RPA", "Cyprus", 12, 32, True, 34.23, 345, 65.653}

print(s1)
print(type(s1))
print(len(s1))

for e in s1:
    print(e)

# duplicate values not printed
s2 = {"Selenium", "Selenium", "derf", 23}
print(s2)

s2.add("Protractor")
print(s2)

s2.remove("derf")
print(s2)

s2.discard(23)
print(s2)

"""
discard :- if item is not present in set and discard used then nothing happen
remove :- if item is not present in set and remove is used then exception arisen
"""

set1 = {"Keshav", "Sharma"}
set2 = {1, 2, 3, 4}

set3 = set1.copy()
print(set3)
set1.clear()
print(set1)
