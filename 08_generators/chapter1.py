# Generators with yield and next methods
# Regular Functions vs Generator Functions
# generator functions are memory efficient and return a single value at a time using yield keyword.
# yield is a keyword that is used to produce a series of values over time, pausing the function's state between each value.

# Generator Function -------------------------------------
def serve_chai(): # generator : difference comes in the way u return values.
    yield "Masala Chai"
    yield "Cardamom Chai"
    yield "Ginger Chai"

stall=serve_chai() # calling the generator function returns a generator object.
print(stall) # <generator object serve_chai at 0x7f9b8c0d4d30>
print("\nIterating over generator object:")
for cup in stall: # iterating over the generator object to get values one by one.
    print(f"Serving: {cup}")
    
# Using next() to get values one by one from generator
stall2=serve_chai() # calling the generator function returns a generator object.
print("\nUsing next():")
print("Serving: ", next(stall2)) # Serving: Masala Chai
print("Serving: ", next(stall2)) # Serving: Cardamom Chai
print("Serving: ", next(stall2)) # Serving: Ginger Chai
# number of next calls should not exceed number of yields in generator function otherwise StopIteration error will occur.

#------------------------------------------------------------------------
    
    
# Normal function that performs same task -----------------
print("\nUsing normal function & returning via list:")
def get_chai_list():
    return ["Masala Chai","Cardamom Chai","Ginger Chai"]
chai_list=get_chai_list() # calling the normal function returns the entire list at once.
print(chai_list) # ['Masala Chai', 'Cardamom Chai', 'Ginger Chai']
for cup in chai_list: # iterating over the list to get values one by one.
    print(f"Serving: {cup}")
    
# -------------------------------------------------------------------