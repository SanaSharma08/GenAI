# Set Comprehensions in Python
# A set comprehension is a concise way to create sets in Python.
# It is similar to list comprehensions but uses curly braces {} instead of square brackets [].
 
# Example: Creating a set of squares of even numbers from 0 to 9

# expression = square**2 since this is the value that we want to add to the set.
# item =square since this is the variable that takes each value from the iterable.
# iterable = range(10) since this is the sequence of values we are iterating over.
# condition = if square % 2 == 0 since this filters the values to include only even numbers.

squares_set={ square**2 for square in range(1,10) if square % 2==0}
print(squares_set)  # Output: {4, 16, 36, 64}


# Comples Example:
recipes ={
    "Masala Chai": ["Tea Leaves", "Milk", "Water", "Spices", "Sugar"],
    "Cardamom Chai": ["Tea Leaves", "Milk", "Water", "Cardamom", "Sugar"],
    "Ginger Chai": ["Tea Leaves", "Milk", "Water", "Ginger", "Sugar"],
    "Tulsi Chai": ["Tea Leaves", "Milk", "Water", "Tulsi Leaves", "Sugar"],
    "Rose Chai": ["Tea Leaves", "Milk", "Water", "Rose Syrup", "Sugar"],
    "Vanilla Chai": ["Tea Leaves", "Milk", "Water", "Vanilla Extract", "Sugar"],
    "Cinnamon Chai": ["Tea Leaves", "Milk", "Water", "Cinnamon", "Sugar"],
    "Honey Chai": ["Tea Leaves", "Milk", "Water", "Honey"],
    "Chocolate Chai": ["Tea Leaves", "Milk", "Water", "Cocoa Powder", "Sugar"],
    "Spiced Almond Chai": ["Tea Leaves", "Milk", "Water", "Almonds", "Spices", "Sugar"]
}
# Task: Create a set of all unique ingredients used across all recipes.

# set only stores unique values, so even if an ingredient appears in multiple recipes, it will only be included once in the final set.

unique_ingredients={ingredients for recipe in recipes.values() for ingredients in recipe} # like nested loops to iterate through each recipe and its ingredients.
print(unique_ingredients)