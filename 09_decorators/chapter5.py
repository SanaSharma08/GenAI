# Decorators in Python
# Decoration is something you do on top of something else
# It's just a wrapper around your function.


# Preserves meta data
from functools import wraps 

def my_decorator(func): # decorator with name my_decorator
    
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

# Following line is basically @ + name of your decorator
@my_decorator # tells us that whatever comes after this needs to be decorated so this line is crucial
def greet():
    print("Hello, from decorators class from python")
    
greet()
print(greet.__name__) # This line will print greet because of @wraps(func) in my_decorator sisnce it preserved the meta data of greet(), if we remove that line, this line would print wrapper as function name.