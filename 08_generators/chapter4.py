# Yield from and close the generator

# Just remember yield == return for generators - it will be easy to understand if u remember that!
# the only difference is return terminates n yield pauses.
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    
def imported_chai():
    yield "Matcha"
    yield "Oolong"
    
def full_menu():
    yield from local_chai()
    yield from imported_chai()
    
menu=full_menu()
count=1
for chai in menu:
    print(f"#{count}. {chai}")
    count+=1
    
def chai_stall():
    try:
        while True:
            order=yield "Waiting for chai order"
    except:
        print("Stall closed!")
stall= chai_stall()
print(next(stall))
stall.close() # Triggers generator exit method
# u should always do this : this cleansup your memory