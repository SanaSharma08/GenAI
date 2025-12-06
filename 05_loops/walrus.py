#Walrus operator example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Using walrus operator to filter and print even numbers
for num in numbers:
    if (even_num := num % 2) == 0:
        print(f"{num} is even.")
#DEfinition of walrus operator: 
# The walrus operator (:=) allows assignment and return of a value in the same expression.


#example 2: Using walrus operator input validation
available_sizes = ["small", "medium", "large", "extra large"]
if(requested_size := input("Enter size (small, medium, large, extra large): ").lower()) in available_sizes:
    print(f"{requested_size} is available.")
    #description: Here, the walrus operator assigns the user input to requested_size and checks if it's in available_sizes in one step.
else:
    print(f"Sorry, {requested_size} is not available.")


#example 3: Using walrus operator in a while loop for flavor selection    
flavours = ["vanilla", "chocolate", "strawberry", "mint", "coffee"]
while(flavor := input("Enter a flavor: ").lower()) not in flavours:
    print(f"Sorry, {flavor} is not available. Please try again.")
print(f"You selected {flavor}, confirmed!")
# description: The walrus operator assigns user input to flavor 
# and checks its availability in one go.