# Build an authorization Decorator
# used in Django all the time.

from functools import wraps

def require_admin(func):
    @wraps(func) # preserve user data
    def wrapper(user_role):
        if(user_role != "admin"):
            print("Access Denied! Adminas Only")
            return None # Default return 
            # Makes your program full-proof 
            # Sometimes, u might encounter errors if u do not explicitely return in all statements inside wrapper, so it is a good practise to include a default return.
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print(f"Access granted to teas inventory!")
access_tea_inventory("user")
access_tea_inventory("admin")