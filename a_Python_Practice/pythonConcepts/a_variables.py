"""
# python have 35 keywords
"""
print("hello python !...")

a = 10  # a is holding value of 10
_a = 20  # start with alphabet / underscore is allowed only, starting with [0-9] not allowed
_A123e = 40  # any char _/[A-Z]/[a-z]/[0-9] can be allowed after letter/underscore
wer123 = 50  # any char _/[A-Z]/[a-z]/[0-9] can be allowed after letter/underscore
if_ = 60  # keywords can not be used as variable names eg: if/else/continue
_b = 60  # this means this variable is declaring as private var
__abc = 100  # if underscore using 2 times then the value of variable cannot be overridden
total_amount = 70  # underscore also using to make things readable
a1, d, g, f = 21, 43, 56, 23  # multiple assigning of variables also possible
r, s, t = 12, 4.67, "keshav"  # different types of vars also used
print(type(r))  # check type of var
print(type(s))  # check type of var
print(type(t))  # check type of var


class A:
    public_var = "public variable"  # public variable :- by-default all are public
    _protected_var = "protected variable"  # protected variable :- can access within {present class and derived class}
    __private_var = "private variable"  # private variable :- can access within {present class only}

# {Protected} and {private} variables can also be accessed outside their scope in Python
# print(ClassName._ProtectedVariableName)
# print(ClassName._ClassName__PrivateVariableName)
