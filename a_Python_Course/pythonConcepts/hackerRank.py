list = [1, 2, 3, 4, 5, 6, 1]
unique = set(list)


duplicate = {n:list.count(n) for n in list if list.count(n) >= 2}
print(duplicate)


