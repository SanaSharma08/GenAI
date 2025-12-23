# Infinite Generators in python
def infinite_chai():
    # simulate a system where u buy tea once and can have infinite refills
    count=1
    while True:
        yield f"Here's your #{count} chai refill! Enjoy!"
        count+=1
    # infinite generator does not have a termination condition
        
refill=infinite_chai()
user2=infinite_chai()

# This is how u control range of infinite generator
for _ in range(5): #limiting to 5 refills for demonstration
    print(next(refill))
    
print("----- User 2 Refills -----")
for _ in range(3): #limiting to 3 refills for demonstration
    print(next(user2))