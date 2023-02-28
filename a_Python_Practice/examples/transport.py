from a_Python_Course.pythonConcepts.o_accessSpecifiers import Car

car = Car()
print(car.public_var)
car.public_method()

# python discourage use of protected var/method outside of class / child class
print(car._protected_var)

# private variables can also be accessed outside of class
# print(car.__private_var)
print(car._Car__private_var)


car.public_method()
car._protected_method()
car._Car__private_method()



