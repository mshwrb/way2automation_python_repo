# *args (Non-Keyword Arguments) - non-key-worded variable length argument list
# **kwargs (Keyword Arguments)
print(
    "--------------------------------------------------------------only "
    "args----------------------------------------------------------------------------------------------------")


def myFunc(*args):
    for n in args:
        print("printing stuff from args: ", n)


myFunc('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print(
    "--------------------------------------------------------------argument with "
    "args----------------------------------------------------------------------------------------------------")


def myFun(arg1, *args):
    print("First argument :", arg1)
    for arg in args:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print(
    "---------------------------------------------------------------only "
    "kwargs------------------------------------------------------------------------------------------")


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

print(
    "---------------------------------------------------------------argumnet with "
    "kwargs------------------------------------------------------------------------------------------")


def myFun(arg1, **kwargs):
    print("first argument: ", arg1)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')
