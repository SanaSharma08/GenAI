# Handling Multiple return Values in Functions
# if a function return nothing - > returns None
# A function can return a single value and even multiple values.
# When multiple values are returned, they are packed into a tuple.
# return can also be used to exit a function early.


#Return nothing example ----------
print("Return Nothing Example:")
def greet_customer(name):
    print(f"Welcome to the Chai Cafe, {name}!")
    
greet=greet_customer("Alice")
print(greet)  # prints None

# Multiple return values example ----------
print("\nMultiple Return Values Example:")
def make_chai():
    # Returns multiple values: tea type, milk type, sugar level
    tea_type = "Masala"
    milk_type = "Whole Milk"
    sugar_level = "Medium"
    return tea_type, milk_type, sugar_level


result = make_chai()
print(result)  # prints a tuple

# Unpacking the returned values ----------
tea, milk, sugar = make_chai()
print(f"Chai Order: {tea} Tea, {milk}, Sugar Level: {sugar}")

# or slice tuple with indexing
tea2=result[0]
milk2=result[1]
sugar2=result[2]
print(f"Chai Order: {tea2} Tea, {milk2}, Sugar Level: {sugar2}")


# Early return example ----------
print("\nEarly Return Example:")
def check_inventory(item):
    inventory = {
        "Masala Chai": 10,
        "Cardamom Chai": 0,
        "Ginger Chai": 5
    }
    if item not in inventory:
        print(f"Item {item} not found in inventory. exiting early.")
        return  # Early exit if item not found
    if inventory[item] <= 0:
        print(f"Sorry, {item} is out of stock. exiting early.")
        return  # Early exit if item is out of stock
    print(f"{item} is available with quantity: {inventory[item]}")
    
check_inventory("Cardamom Chai") # early
check_inventory("Tulsi Chai") # early
check_inventory("Ginger Chai")