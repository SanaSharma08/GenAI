# USECASE OF FUNCTIONS 
# 1- Reducing code duplication

# You're managing a busy tea stall.
# You receive many orders and want to print each customer's name
# along with the type of chai they ordered.
# Task:
# • Write a function print_order(name, chai_type)
# • Call it multiple times for different customers


def print_order(name, chai_type):
        print(f"Order for {name}: {chai_type} Chai")

while(name := input("Enter customer name (or 'exit' to stop): ")) != 'exit':
    chai_type = input(f"Enter chai type for {name}: ")
    print_order(name, chai_type)
print("Thank you! All orders have been processed.")



# 2- Splitting complex problems into smaller parts


# You're creating a monthly report for a cafe's sales.
# Instead of putting all logic in one place, break it down.
# Task:
# Write a function generate_report() that calls:
# fetch_sales()
# filter_valid_orders()
# summarize_data()

#Defining Functions ----------------------------------
def fetch_sales():
    # Dictionary: menu items as keys, monthly sales as values (in dollars)
    menu_sales_dollars = {
        "Masala Chai": 1200,
        "Cardamom Chai": 950,
        "Ginger Chai": 1100,
        "Tulsi Chai": 700,
        "Rose Chai": 650,
        "Saffron Chai": 400,
        "Vanilla Chai": 800,
        "Cinnamon Chai": 900,
        "Honey Chai": 500,
        "Chocolate Chai": 750,
        "Chai Latte": 1300,
        "Matcha Latte": 1050,
        "Pumpkin Spice Chai": 0,
        "Lemongrass Chai": 0,
        "Apple Spice Chai": 0
    }
    return menu_sales_dollars        
def filter_valid_orders(sales,menu_mrp):
    # Filter out items with zero sales
    # Empty dictionary to store only valid orders
    valid_orders = {}
    for item, amount in sales.items():
        if amount > 0: 
            #calculating total number of orders for each item from valid_orders by dividing total amount by mrp of indiviadual item.
            valid_orders[item] = amount//menu_mrp[item]
    return valid_orders

def summarize_data(valid_orders,sales):
    total_orders=0
    total_money=0
    for item,order in valid_orders.items():
        total_orders+=order
        total_money+=sales[item]
    print(f"You made a total of {total_orders} orders generating ${total_money} in sales this month.")
    
def generate_report():
    #Calling all functions inside generate_report
    sales=fetch_sales()
    valid_orders=filter_valid_orders(sales,menu_mrp)
    summarize_data(valid_orders,sales)
    
    
    sorted_orders = dict(sorted(valid_orders.items(), key=lambda x: x[1], reverse=True))
    print("Top Selling Items This Month:")
    rank=1
    for item,orders in sorted_orders.items():
        print(f"{rank}. {item}: {orders} orders")
        rank+=1

#Defining Functions Ends ----------------------------------       
# code outside of functions

menu_mrp = {
        "Masala Chai": 25,
        "Cardamom Chai": 30,
        "Ginger Chai": 28,
        "Tulsi Chai": 22,
        "Rose Chai": 27,
        "Saffron Chai": 35,
        "Vanilla Chai": 26,
        "Cinnamon Chai": 29,
        "Honey Chai": 32,
        "Chocolate Chai": 33,
        "Chai Latte": 40,
        "Matcha Latte": 45,
        "Pumpkin Spice Chai": 38,
        "Lemongrass Chai": 24,
        "Apple Spice Chai": 36
    }

#calling the main function to generate report
generate_report()