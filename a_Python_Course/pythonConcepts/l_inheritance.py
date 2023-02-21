"""
Inheritance:-
1. Parent
2. child
a. Multilevel inheritance supported   A ----> B ----> C -----> D
b. Multiple inheritance supported
    A       B
    |       |
     |     |
      |   |
       |  |
        ||
         C
"""


class Addition():  # Base class / Parent class
    name = "Keshav Sharma"

    def __init__(self, aa):
        self.aa = aa
        print(self.aa)

    def add(self):
        print("adding 2 numbers")


class Subtraction(Addition):  # derived class / child class also inheriting the properties of parent class
    def __init__(self, ss, aa):
        super().__init__(aa)
        self.ss = ss
        print(self.ss)

    def subtract(self):
        print("subtracting 2 numbers")


class Divide(Subtraction):
    def __init__(self, dd, ss, aa):
        super().__init__(ss, aa)
        self.dd = dd
        print(self.dd)

    def divide(self):
        print("dividing 2 numbers")


class Equate:
    def __init__(self, ee):
        self.ee = ee
        print(self.ee)

    def Equate(self):
        print("equate two numbers")


class Multiply(Addition):  # which ever classname appears first would call method from that class
    def __init__(self, mm, aa):
        super().__init__(aa)
        self.mm = mm
        print(self.mm)

    def multiply(self):
        print("multiplying 2 numbers")


class Float(Addition, Equate):  # which ever classname appears first would call method from that class
    def __init__(self, ff, aa, ee):
        Addition.__init__(self, aa)
        Equate.__init__(self, ee)
        self.ff = ff
        print(self.ff)

    def Float(self):
        print("multiplying 2 numbers")


obj = Float("ff", "aa", "ee")
