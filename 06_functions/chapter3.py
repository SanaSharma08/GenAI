#Scopes  & Named spaces
# A scope is a region of a program where a particular named variable can be accessed.

#Scopes and Name Resolution
# In Python, there are four types of scopes:
# Local Scope: Variables defined within a function.
# Enclosing Scope: Variables in the local scope of enclosing functions. (from outer function if nested functions are present)
# Global Scope: Variables defined at the top level of a module or declared global using the global keyword.
# Built-in Scope: Names preassigned in the built-in names module.

#Eg 1 -----------------------------------------
def serve_chai():
    chai_type = "Masala Chai"  # Local scope

    def prepare_chai():
        # Enclosing scope
        print(f"Preparing {chai_type}...")

    prepare_chai()
    print(f"Serving {chai_type}!")
    
chai_type = "Cardamom Chai"  # Global scope
serve_chai()
print(f"Global chai type is {chai_type}.")  # Accessing global scope

#Example 2 -------------------------------------------
def chai_counter():
    chai_order="Ginger Chai" # Local scope
    def print_order():
        chai_order="Tulsi Chai" # Enclosing scope
        print(f"Preparing {chai_order}...") # Enclosing scope
    print_order() # Calling nested function
    print(f"Order received for {chai_order}.") # Local scope
chai_order="Rose Chai" # Global scope
chai_counter()
print(f"Today's special is {chai_order}.") # Global scope