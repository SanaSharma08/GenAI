import recipes.flavors 
# or
# Named import
# from recipes.flavors import elaichi_chai, ginger_chai, tulsi_chai, rose_chai
# or 
# from .recipes.flavors import elaichi_chai, ginger_chai, tulsi_chai, rose_chai


print("Welcome to the Chai Business!")
fl1=recipes.flavors.elaichi_chai()
fl2=recipes.flavors.ginger_chai()
fl3=recipes.flavors.tulsi_chai()
fl4=recipes.flavors.rose_chai()
menu=[fl1,fl2,fl3,fl4]
