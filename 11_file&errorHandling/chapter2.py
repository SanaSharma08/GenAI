# Handling Multiple Errors

def process_order(item,quantity):
    try:
        price={"masala":20}[item] # similar to dict[key] where dict is a dictionary and item in this context is the key.
        cost=price * quantity
        # Good example usecase of raise
        # * operator works on string so "6"*4="6666"
        # so this will not raise a typeerror automatically
        # But I want to raise the error, so I write my custome error that is raised id type of quantity is not a number.
        # So the except block will catch it and it will be handled!
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a number. Try Again!")
    except KeyError as k: # Exception 1
        print("Sorry! that chai is not available")
    except TypeError as t: # Exception 2
        print("Error: ",t)
    else:
        print(f"total cost is {cost}")
    finally:
        print("Have a great day!")
 
print("\nValid Case:")       
process_order("masala",5) 
# total cost is 100
# Have a great day!

print("\nValueError Case:")  
process_order("ginger",1)
# Sorry! that chai is not available
# Have a great day!

print("\nTypeError Case:")  
process_order("masala","6")
# Error:  Quantity must be a number. Try Again!
# Have a great day!