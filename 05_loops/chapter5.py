menu = [
    "Green Tea",
    "Black Tea",
    "Chamomile Tea",
    "Earl Grey",
    "Oolong Tea",
    "Jasmine Tea",
    "Peppermint Tea",
    "Chai Latte",
    "Matcha Latte",
    "London Fog",
    "English Breakfast",
    "Darjeeling"
]
# Using Enumerate to print menu items with their index
for index,item in enumerate(menu,start=1):
    print(f"{index}. {item}")
#General loop to print menu items
for item in menu:
    print(f"Menu item: {item}")