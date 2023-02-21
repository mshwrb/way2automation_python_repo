str = "I love india"

str = str.split()
reverse_str = str[::-1]
str1 = " "
print(str1.join(reverse_str))

string_new = " ".join([ele for ele in reverse_str])
print(string_new)

i_1 = [1, 2, 3, 4]
i_2 = [1, 44, 99, 166]
output = [(1, 1), (2, 44), (3, 99), (4, 166)]

mapped = zip(i_1, i_2)
print(list(mapped))

for i, (i_1, i_2) in enumerate(zip(i_1, i_2)):
    print(i, i_1 + i_2)


asdf = [2, 5, 2, 7, 4]

lst_new = []
lst_new_1 = []
for i in range(len(asdf)-1):
    lst_new.append(abs(asdf[i] - asdf[i+1]))
lst_new = list(set(lst_new))
print(len(lst_new))


