# Dictionary Comprehensions in python
# {key: value for item in iterable if condition}

tea_prices_inr={
    "Masala Chai": 150,
    "Cardamom Chai": 120,
    "Ginger Chai": 130,
    "Tulsi Chai": 100,
    "Rose Chai": 90,
    "Saffron Chai": 80,
    "Vanilla Chai": 110,
    "Cinnamon Chai": 115,
    "Honey Chai": 95,
    "Chocolate Chai": 125,
    "Chai Latte": 160,
    "Matcha Latte": 140,
    "Pumpkin Spice Chai": 0,
    "Lemongrass Chai": 0,
    "Apple Spice Chai": 0
}
# Convert prices from INR to USD (1 USD = 90 INR) using dictionary comprehension
tea_prices_usd={tea:price_inr//90 for tea,price_inr in tea_prices_inr.items()}

# trick : start writing from the for loop part first
# then add the key:value part in the beginning
print(tea_prices_usd)