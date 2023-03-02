"""
Constructor :- They are first function of class
syntax : __intit__()
1. All classes have this function by-default
2. It's been called when class is initiated / object of class is created
3. first parameter is "self" it represents the current object
4. Constructor overloading not possible eg:
   def __init__(self, name, id):
        self.id = id  # assigning value of local var to global var
        self.name = name
      def __init__(self, name, id, age):
        self.id = id  # assigning value of local var to global var
        self.name = name
"""


class Practice:
    def __init__(self):
        print("Inside Constructor")

    def add(self):
        print("Adding something")


# a = Practice()
# a.add()

"""
self.id / self.name :- global variable
"""


class Employee:
    def __init__(self, name, id):
        self.id = id  # assigning value of local var to global var
        self.name = name
        self.a = id

    def display(self):
        print("Name is :", self.name)
        print("ID is :", self.id)
        print("age is :", self.a)


# e = Employee("Keshav", 101, 24)
# e.display()


