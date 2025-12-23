# self argument in python

class Chaicup:
    size=150 #ml
    
    def describe(self): 
        # self keyword allows class methods to access all attributes of the class.
        # it is like a reference object for internal attributes
        return f"A {self.size} ml chai cup"
    
    
cup=Chaicup()
cup.size=200
print(cup.describe())
#print(Chaicup.describe()) # will not work since methods need context to run. Here the object_name acts as a  (it is assumed that the values of attributes might change from each object and that might affect the output of the method). So, Calling a a method directly by classname is not recommended.
# so always makae objects!