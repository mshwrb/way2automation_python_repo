"""
Exceptions / Errors
Exceptions : simply disruption in the program
Errors     :
   compile-time :- when we compile-program(program code converted to machine code) and encountered any error
   run-time :- when we run-program(program is running and occurs after compilation) and encountered any error

Try and Except block
python specific : try , Except and Else
try , Except , Else , finally
Types of exceptions :
PYTHON EXCEPTION HIERARCHY :-
BASE EXCEPTION:
   1. Exception
        a. Attribute exception / error
        b. Arithmatic exception / errors
             1. ZeroDivision error
             2. FloatingPoint error
             3. Overflow error
        c. EOF exception (End of file)
        d. Name exception
   2. System Exit (something wrong with os part)
   3. Generator Exit
   4. Keyboard Interrupt
"""
try:
    print("opening file")
    a = int(input("Enter the value for first number "))
    b = int(input("Enter the value for second number "))
    c = a / b
    print(f"Result is {c}")
except (ZeroDivisionError, ValueError):
    print("error occurred in file")
    print("please enter a valid number")
else:
    print("inside an else block")  # this will execute only if try doesn't yield to exception
    print("closing file")
finally:
    print("I am always executed")

print("out side try/except block")
