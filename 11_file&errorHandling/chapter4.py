# Create your own exceptions

# Remember an error is a mihap in code, and exceptions are errors that have been handled.

#Errors are generally beyond the control of the program itself and signify a critical failure that prevents the application from continuing its normal operation.

#Exceptions represent conditions that a reasonable application might try to catch and handle.


# A custom class that inherits Exception class - viola! you just made an exception apart from pre defined exceptions! 
class OutOfIngredientsError(Exception):
    pass

def make_chai(milk,sugar):
    if milk==0 or sugar==0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("Chai ready!")
    
make_chai(7,0) # OutOfIngredientsError