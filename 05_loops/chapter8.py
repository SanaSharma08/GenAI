# Some chai flavors are out of stock.
# You want to skip those and stop entirely if
# someone requests a restricted flavor.
# Task:
# • Skip if flavor is "Out of Stock" - continue
# • Break if flavor is "Discontinued" - break

out_of_stock = [
	"Ginger Chai",
	"Tulsi Chai",
	"Rose Chai",
]

discontinued = [
	"Saffron Chai",
	"Chai de Luxe",
]

menu = [
	"Masala Chai",
	"Cardamom Chai",
	"Ginger Chai",
	"Tulsi Chai",
	"Rose Chai",
	"Vanilla Chai",
	"Cinnamon Chai",
	"Saffron Chai",
	"Chai de Luxe",
	"Honey Chai",
	"Chocolate Chai",
	"Spiced Almond Chai",
]


for flavor in menu:
    if flavor in out_of_stock:
        print(f"Sorry, {flavor} is currently out of stock. Skipping...")
        continue # skip to next iteration
    elif flavor in discontinued:
        print(f"Alert: {flavor} has been discontinued. Stopping orders.")
        break # Terminate the loop entirely & no further items are printed.
    print(f"{flavor} is available for order.")
print("Order processing complete.") # runs when loop ends normally or via break.
    # else command not needed since break n continue will automatically terminate the current iteration.