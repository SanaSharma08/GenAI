# List comprehensions in python
# [expression for item in iterable if condition]
# expression is the value to be added to the new list.
# item is the variable representing each element in the iterable.
# iterable is the collection being looped over.
# condition is an optional filter that determines whether the expression is included in the new list.

menu=[
    "Masala Chai",
    "Cardamom Chai",
    "Ginger Chai",
    "Tulsi Chai",
    "Rose Chai",
    "Iced Lemon Tea",
    "Iced Peach Tea",
    "Iced Mint Tea",
    "Iced Green Tea"
]

# expression = tea
# item = tea
# iterable = menu
# condition = "Iced" in tea
# expression name should be same as item name.

iced_tea_menu=[tea for tea in menu if "Iced" in tea]
print("Iced Tea Menu:")
print(iced_tea_menu)


even_numbers=[num for num in range(30) if num %2==0]
print(even_numbers)
