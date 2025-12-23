# Class & object namespace

class Chai:
    origin="India"
 
print(Chai.origin)   
Chai.is_hot=True # adding a new property to class
print(Chai.is_hot)


# Another object

masala=Chai()
masala.is_hot=False # this change will be made in masala object only
print(f"Masala origin: {masala.origin}")
print(f"Masala is hot: {masala.is_hot}")
masala.flavor="All-Spice" # this change is only made in this object
print(f"Masala Flavor: {masala.flavor}")

print(Chai.flavor) # gives error since changes made in masala object won't affect class definition
