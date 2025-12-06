#USECASE 3 - Hiding Implementation Details

# You're building a simple app that registers users.
# You want to separate concerns: getting input, validating it, and saving it.
# Task:
# Write register_user() that calls:
# get_input()
# validate_input()
# save_to_db()

def get_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    return name, email
def validate_input(name,email):
    if "@" not in email or "." not in email:
        print("Invalid email format. Please try again(eg: johndoe@gmail.com)")
        name, email = get_input()
        return validate_input(name,email) #recursion to re-validate input
    else:
        return name, email
def save_to_db():
    name, email = get_input()
    v_name, v_email = validate_input(name,email)
    # Simulating saving to a database
    print(f"Saving {v_name} with email {v_email} to the database...")
    user_details[v_name]=v_email
    print("User registered successfully!")

def show_db(user_details):
    print("Current Users in Database:")
    for name, email in user_details.items():
        print(f"Name: {name}, Email: {email}")
  
user_details={}      
save_to_db()
show_db(user_details)


#USECASE 4 - Improving Readability
# You sell different chai sizes.
# Instead of writing formulas everywhere. create a function.
# Task:
# Write calculate_bill(cups,price_per_cup,size)
# • Return total bill
# • Use this function for multiple orders

def calculate_bill(cups,price_per_cup,size):
    if size not in price_per_cup:
        print("Invalid size. Please choose 's', 'm', or 'l'.")
        return None
    total_bill = cups * price_per_cup[size]
    return total_bill

size=input("Enter chai size (s/m/l): ").lower()
cups=int(input("Enter number of cups: "))
price_per_cup={
    's': 3.00,
    'm': 4.50,
    'l': 6.00
}
bill=calculate_bill(cups,price_per_cup,size)
print(f"Total bill for {cups} {size.upper()} chai(s): ${bill:.2f}" if bill is not None else "Could not calculate bill due to invalid size.")


#USECASE 5 - Improving Traceability
# ur shop adds a 10% VAT on every order
# u want this to be consistent and traceable
# ask:
# • Write add_vat(price, vat_rate)
# • Use it to compute final prices for 3 orders

def add_vat(price, vat_rate=0.10):
    vat_amount = price * vat_rate
    final_price = price + vat_amount
    return final_price

orders = [15.00, 22.50, 9.75]  # Example order prices before VAT
for i, order_price in enumerate(orders, start=1):
    final_price = add_vat(order_price)
    print(f"Final price for order {i} (before VAT: ${order_price:.2f}): ${final_price:.2f}")