# Error Handling

def order(flavor):
    # Tea Flavors Dictionary
    tea_flavors = {
        "Green": 3.50,
        "Black": 3.00,
        "Oolong": 4.00,
        "Herbal": 3.75,
        "Chamomile": 3.25,
        "Peppermint": 3.50,
        "Ginger": 4.25,
        "Jasmine": 4.50
    }

    try: # logic
        order=tea_flavors["Rose"]
    except KeyError: # excepting error
        print("They flavor that you are trying to order, does not exist.")
    else: # executes if execution happened without error
        print(order)
    finally:  # Always Prints
        print("Thank you!")
        
def serve(flavor):
    try:
        print(f"Order received for {flavor} Chai!")
        if(flavor=="unknown"):
            raise ValueError("Not Available! Try Again")
    
    except ValueError as e:
        print("Error: ",e)
    else:
        print(f"Serving {flavor} ....")
    finally:
        print("Thank you!")
        
# serve("ginger")
# Order received for ginger Chai!
# Serving ginger ....
# Thank you!

serve("unknown")
# Order received for unknown Chai!
# Error:  Not Available! Try Again
# "Error: " comes from except block
#  "Not Available! Try Again" comes from raise that is stored in e
# Thank you! - printed from finally