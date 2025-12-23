# Handling Arguments in functions
#Arguments are values passed into functions to customize their behavior.
# They allow functions to process different inputs without changing their internal code.

# 2 types of arguments:
#   1- *args : args stands for "arguments" and allows a function to accept any number of positional arguments.
#   2- *kwargs : keyword arguments allow a function to accept any number of "named" arguments (key-value pairs).


#positional arguments and keyword arguments -------------------------------
def order_tea(tea_type, size, quantity):
    print(f"Order Details: {quantity} cup(s) of {size} {tea_type}")
order_tea("Masala Chai", "Large", 2) #positional arguments
order_tea(size="Medium", tea_type="Cardamom Chai", quantity=1) #keyword arguments (named arguments).

# Example of args -------------------------------
def calculate_total(*prices):
    total = 0
    for price in prices:
        total += price
    return total

total_amount = calculate_total(5.99, 12.49, 3.50)
print(f"Total Amount: ${total_amount:.2f}")

# Example of kwargs -------------------------------
def display_order(**order_details):
    #kwargs collects keyword arguments into a dictionary
    for key, value in order_details.items():
        print(f"{key}: {value}")
display_order(item="Masala Chai", size="Large", quantity=2, price=5.99)


# Combining args and kwargs --------------------------------
def process_order(*items, **details):
    # items is a tuple of positional arguments
    # details is a dictionary of keyword arguments
    print("Order Items: ",items)
    print("Order Details: ",details)
process_order("Masala Chai", "Cardamom Chai", size="Medium", quantity=2, price=11.98) # size, quantity, price are keyword arguments (named arguments).
# In this example, process_order accepts any number of items as positional arguments and any number of order details as keyword arguments.
