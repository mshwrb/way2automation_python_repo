"""
Polymorphism : "Many Forms" , Base for any polymorphism is inheritance, [parent ----> child] => Relationship
1. Operator Overloading , supported
2. Method Overloading / constructor Overloading , not supported
3. Method Overriding
3. Constructor Overloading and Overriding

 # decorator --> @classmethod / @staticmethod
"""


# -------------------------------------------Operator_Overloading--------------------------------------------------------

class OperatorOverloading:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        total_pages = self.pages - other.pages
        return total_pages


object_1 = OperatorOverloading(10)
object_2 = OperatorOverloading(5)

print("--------------------------------------operator overloading---------------------")
print(object_1 + object_2)
print("--------------------------------------operator overloading---------------------")


# ------------------------------------------Method Overloading----------------------------------------------------------

# Not allowed
class MethodOverloading:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)


# class ConstructorOverloading:
#     def __init__(self):
#         print("inside first constructor")
#
#     def __init__(self):
#         print("inside first constructor")

# ------------------------------------------Method/constructor OverRiding----------------------------------------------

class MethodOverridingBase:
    def __init__(self):
       print("base class constructor")

    def a(self):
       print("inside base class")


class MethodOverridingDerived(MethodOverridingBase):
    def __init__(self):
        super().__init__()
        print("child class constructor")

    def a(self):
        super().a()
        print("inside derived class")

    # if want to access parent class property only
    def b(self):
        super().a()


# x = MethodOverridingDerived()
# x.a()  # accessing function in child and parent class
# x.b()  # accessing function in only parent class

# ------------------------------------------Class/Instance Variables----------------------------------------------------

class Dog:
    # Class/static variables
    legs = 4

    def __init__(self):
        # Instance Variables
        self.name = "Milo"
        self.color = "White"

    def get_dog_name(self):
        print(self.name)

    # class method
    @classmethod
    def get_legs_count(cls):
        print(cls.legs)

    @staticmethod
    def general_information():
        print("beware of dogs")

D1 = Dog()
D2 = Dog()

print(D1.name, D1.color, D1.legs, Dog.legs)

D2.name = "Bruno"
D2.color = "Brown"
D2.legs = 5
print(D2.name, D2.color, D2.legs, Dog.legs)
D1.get_dog_name() # instance method
D1.get_legs_count() # class method
Dog.get_legs_count() # only ran when decorator added on top of class method
Dog.general_information() # static level method

# ---------------------------------------------------------------------------------------------------------------------
"""
 3 types of methods / functions / variables
  1. Instance methods / functions / variables  - used to access instance variable of the class 
  2. Class methods / functions / variables - used to access static of the class
  3. Static methods / functions / variables - standalone methods
"""
