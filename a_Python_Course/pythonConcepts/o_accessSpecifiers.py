"""
3 types of access specifiers :
1. public     : by-default all are public
2. private    : __ added to make private
          eg:   __var_name , __method_name
       scope:   can access within {present class}
3. protected  : _ added to make it protected
          eg:   _var_name , _method_name
       scope:   can access within {present class and derived class}
"""


class Car:
    public_var = "public variable"
    _protected_var = "protected variable"
    __private_var = "private variable"

    def __init__(self):
        print("inside Car class constructor ")

    def public_method(self):
        print("inside public method")

    def _protected_method(self):
        print("inside protected method")

    def __private_method(self):
        print("inside private method")
