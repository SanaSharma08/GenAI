# send Values to a Generator : vv.imp concept
# This implementation of infinite generator is widely used in scenarios like handling user inputs, processing streams of data, or managing stateful interactions in applications.
def chai_customer():
    print("Welcome to the Chai Cafe! What chai would you like today?")
    order= yield "Please enter your chai order:"
    while True:
        print(f"Preparing your {order}...")
        order = yield f"Your {order} is ready! What chai would you like next?"
        
stall = chai_customer()
prompt = next(stall)  # Start the generator
# since no value is sent, it runs till first yield and never really runs the while loop.
# In order to run the while loop, we need to send a value to the generator.
print(prompt)
orders = ["Masala Chai", "Ginger Chai", "Cardamom Chai"]

# Sending orders to the generator
for order in orders:
    # stall reference to generator Object
    response = stall.send(order) # Send order to generator
    print(response)