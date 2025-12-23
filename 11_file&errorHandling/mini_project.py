# Mini Project: Bill App
class FlavorOutOfStock(Exception): pass
class OutOfIngredients(Exception): pass



def generate_bill(flavor,quantity=1,milk=12,sugar=10):
    # Tea Flavors Dictionary (price per cup in USD)
    tea_flavors = {
        "Green Tea": 3.50,
        "Black Tea": 3.00,
        "Oolong Tea": 4.00,
        "Herbal Tea": 3.75,
        "Chamomile": 3.25,
        "Peppermint": 3.50,
        "Ginger Tea": 4.25,
        "Jasmine Tea": 4.50,
        "Rose Tea": 6.90
    }
    # Tea stock levels (cups available)
    tea_stock = {
        "Green Tea": 20,
        "Black Tea": 0,
        "Oolong Tea": 15,
        "Herbal Tea": 25,
        "Chamomile": 10,
        "Peppermint": 0,
        "Ginger Tea": 12,
        "Jasmine Tea": 8,
        "Rose Tea": 5
    }
    
    try:
        if(tea_stock[flavor] ==0):
            raise FlavorOutOfStock("Sorry! Flavor Is Out Of Stock")
        elif(milk ==0 or sugar==0):
            raise OutOfIngredients("Sorry! We'll be back soon")
        elif not isinstance(quantity, int): # correct way to check type since type() function returns the type object of a variable 
            raise ValueError("quantity must be int!")
        total=tea_flavors[flavor] * quantity
        # print(sana) This line will raise NameError that will be executed by except Exception as e
    except KeyError as k:
        print("Sorry! This flavor is unaivailable. Try Again")
    except ValueError as v:
        print("Sorry! ",v)
    except Exception as e: # Handling all other
        print("Error: ",e)
    else:
        print("Order Total: ", total)
    finally:
        print("Namaste")
        
# generate_bill("Peppermint",3) #FlavorOutOfStock: Sorry! Flavor Is Out Of Stock
# generate_bill("Masala",8)  #Sorry! This flavor is unaivailable. Try Again
# generate_bill("Rose Tea",10,0)  #OutOfIngredients: Sorry! We'll be back soon   
# generate_bill("Rose Tea","9") #Sorry!  quantity must be int!
generate_bill("Jasmine Tea",5)
# Order Total:  22.5
# Namaste  
    
