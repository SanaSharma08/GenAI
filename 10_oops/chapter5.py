# Contructors & init in python

class ChaiOrder:
    # __init__ method is automatically called whenever an instance is created!
    def __init__(self,type_,size): 
        # type_ just differenciates variable name from keyword type
        # This __init__ method initializes type n size for each object
        self.type=type_
        self.size=size
    def summary(self):
        return f"{self.size} ml of {self.type} chai"
 
# With __init__   
order=ChaiOrder("Masala",220) # values of attributes can be passed on as arguments
print(order.summary())

# Without __init__
# order=ChaiOrder()
# ChaiOrder.type_="Masala"
# ChaiOrder.size=200