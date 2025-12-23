# Build Logger with Decorator

from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args,**kwargs): # allowsus to not care about the number of arguments, we can accept any number of args n named args.
        print(f"Calling: {func.__name__}")
        result =func(*args,**kwargs)
        print(f"Finished: {func.__name__}")
        return result
        
    return wrapper

@log_activity  # name of our decorator is log_activity
def brew_chai(type):
    print(f"Brewing {type} Chai.....")

brew_chai("Rose")