# chapter 8
# Built-in Functions

def chai_flavor(flavor="Masala Chai"):
    # You can write function documents within triple qoutes at the start of the function - good practise.
    """Returns a message indicating the selected chai flavor."""
    return f"You have selected {flavor}."

print(chai_flavor.__doc__)  # prints documentation string
print(chai_flavor.__name__)  # prints function name



# Documentation Strings and Function Metadata

def generate_bill(chai=0,samosa=0):
    """
    Generates and prints the bill for chai and samosa orders.

    Args:
        chai (int, optional): _description_. Defaults to 0. No. of chai ordered. 1o rupees each.
        samosa (int, optional): _description_. Defaults to 0. No. of samosas ordered. 15 rupees each.
    Returns:
        float: Total bill amount.
    """
    total = (chai * 10) + (samosa * 15)
    return total

print(generate_bill.__doc__)  # prints documentation string
print(generate_bill.__name__)  # prints function name
print(f"Total bill amount: ${generate_bill(2,3)}")  # Example call to the function