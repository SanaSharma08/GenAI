#3 Ways to Access Base Class

class Chai:
    # BASE CLASS
    def __init__(self,type_,strength):
        self.type=type_
        self.strength=strength
        
class GingerChai(Chai):
    
    # Code Duplication for writing new contructor
    def __init__(self, type_, strength,spice_level):
        self.type=type_
        self.strength=strength
        self.spice_level=spice_level
        
class TulsiChai(Chai):
    # Explicit Calling from Base class
    def __init__(self, type_, strength,sweetness):
        Chai.__init__(self,type_, strength) # passing self is important for proper mapping of arguments
        self.sweetness=sweetness
        
class RoseChai(Chai):
    # super() method: means that u wanna call the constructor from the base class.
    def __init__(self, type_, strength, intensity):
        super().__init__(type_, strength)
        self.intensity=intensity
        
 
print("\nRoseChai class & Super() method: ")       
r_chai=RoseChai("Kulhad","Kadak","Super Red")
print(r_chai.type)
print(r_chai.strength)
print(r_chai.intensity)


print("\nGingerChai class & Duplication: ")       
g_chai=GingerChai("Cutting","Mild","spicy")
print(g_chai.type)
print(g_chai.strength)
print(g_chai.spice_level)


print("\nTulsiChai class & Explicit Calling: ")       
t_chai=TulsiChai("Kulhad","Mild","Sweet")
print(t_chai.type)
print(t_chai.strength)
print(t_chai.sweetness)