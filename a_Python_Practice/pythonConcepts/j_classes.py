"""
OOPS, Concepts / Procedural language (step by step implementation of code)
1. Classes
2. Objects
3. Encapsulation
4. Abstraction
5. Inheritance
6. Polymorphism

class :- it is a blueprint/template which describes behaviour/state
 - contains variables, functions, constructors

self :-
1. it is the keyword through which we can access the attributes and methods of class in python
2. The first parameter of every function must contain self then after , we can have different params

Objects :- Instance of class

functions :-
myfunc(asdf1, asdf2, asdf3 = " ", asdf4=" ")
- mandatory parameters :- asdf1 and asdf2
- optional parameters :- asdf3 and asdf4
"""


class Humans:
    eyes = "blue"
    nose = "Large"

    def legs_function(self):
        print("there are 4 legs of animals")

    def eys_function(self, color):
        print(f"This is the function to see - {color}")

    def noes_function(self, size):
        print(f"this is the function to smell - {size}")

    def ear_function(self, sound):
        print(f"this is the function to hear - {sound}")



a = Humans()
a.legs_function()
a.eys_function("Black")
a.ear_function("Round")
a.noes_function(15.34)


