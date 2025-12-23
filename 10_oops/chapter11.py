# Property decorator - Getter and Setter
# @property decorator for creating Getter and Setter methods
#The @property decorator allows you to define methods that can be accessed like attributes (variables), providing a clean, "Pythonic" way to enforce rules and hide the internal implementation details of your class. This is part of the concept of encapsulation.

class TeaLeaf:
    def __init__(self,age):
        self._age=age
        
    @property # getter
    #This method is now responsible for reading the value of the age attribute.
    #When you access leaf.age, this method is automatically called.
    def age(self):
        return self._age+2
    #Notice it returns self._age + 2. This demonstrates that the property doesn't just return the stored value; it can perform a calculation. For example, if _age is the age in years, the property age might represent the harvest maturity age (stored age + 2 years of processing).
    
    @age.setter #setter 
    #This method is responsible for writing (setting) a new value to the attribute.
    #When you write leaf.age = 4, this method is automatically called with 4 passed as the age argument.
    def age(self, age):
        #This is the most crucial part. The setter enforces validation logic. It ensures that the internal state (self._age) can only be set to a value between 1 and 5. If an invalid value is provided, it raises an error, protecting the integrity of your object's data.
        if 1<= age <=5:
            self._age=age
        else:
            raise ValueError("Must be b/w 1 & 5")
        
leaf=TeaLeaf(2) # 1. Initializes internal _age = 2
# Accessing the property (Getter is called)
print(leaf.age) # 2. Calls the 'def age(self):' method
                #    Returns self._age + 2 (which is 2 + 2 = 4)
# Setting the property (Setter is called)             
# leaf.age = 6 #the setter throws a ValueError! so comment out for now
leaf.age = 3 # Calls the '@age.setter' method, self._age is updated to 3

# Accessing again
print(leaf.age)    # Calls the getter again
                   # Returns self._age + 2 (which is 3 + 2 = 5)
# Output: 5