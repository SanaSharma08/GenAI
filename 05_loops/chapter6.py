#Task:
# Use two lists: one for names and one for bills.
# Print: "[Name) paid $[Bill amount]" for each name and bill amount pair.

names = [
    "Alice",
    "Benjamin",
    "Charlotte",
    "David",
    "Emma",
    "Frank",
    "Grace",
    "Henry",
    "Isabella",
    "Jack",
    "Katherine",
    "Liam"
]
bills = [15.50, 22.00, 18.75, 25.30, 20.10, 17.85, 28.40, 19.95, 23.60, 16.20, 21.75, 26.50]

#Solving using zip to pair names with their corresponding bills
for name, bill in zip(names, bills):
    print(f"{name} paid ${bill:.2f}")