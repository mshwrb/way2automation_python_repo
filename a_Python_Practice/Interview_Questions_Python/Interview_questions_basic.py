# Q1 Join 2 tuples together with zip function
list1 = [1, 2, 3, 4, 5]
list1a = [1, 2, 3, 4, 5]
asdf1 = zip(list1, list1a)
output1 = list(asdf1)
# print(output1)

# Q2 Find the Count of chars with respect to chars
list2 = ['a', 'b', 'c', 'd', 'a', 'c', 'd', 'b', 'b', 'a']
asdf2 = {n: list2.count(n) for n in list2}
# print(asdf2)

# Q3 Remove all elements which are duplicate in the list
list3 = ['a', 'b', 'c', 'd', 'a', 'a']
duplicate_item = 'a'
asdf3 = [n for n in list3 if n != duplicate_item]
# print(asdf3)

# Q4 Remove all elements which are duplicate in the list except 1
list4 = ['a', 'b', 'c', 'd', 'a', 'a']
duplicate_item = 'a'
output4 = list((set(list4)))
# print(output4)

# Q5 Reverse words from string with words position fixed
list5 = "My Name is Keshav Sharma"
b = ""
list_of_words = list5.split(" ")
for n in list_of_words:
    a = n[::-1]
    b = b + a + " "
# print(b)

# Q6 Reverse complete string
string6 = "I am a python programmer"
words = string6.split()
words = list(reversed(words))
# print(" ".join(words))

# Q7 Write a palindrome of string
string7 = "madam"
if string7 == string7[::-1]:
    print(f"{string7[::-1]} and {string7} are equal")
