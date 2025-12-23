# Lambdas, Pure Functions, Impure Functions

# Type of Functions:
# 1- Lambda Functions: Small anonymous functions defined with the lambda keyword.
# 2- Pure Functions: Functions that always produce the same output for the same input and have no side effects.
# 3- Impure Functions: Functions that may produce different outputs for the same input or have side effects.
# Recursive Functions: Functions that call themselves to solve smaller instances of the same problem.

# Pure vs Impure Functions Example--------------
# Pure Function Example
def pure_add(x, y):
    # This function always returns the same output for the same inputs and has no side effects.
    # This means it doesn't modify any external state or variables.
    return x + y

#Impure Function Example : not recommended
total_chai=0
def impure_add(x):
    # This function modifies an external variable (total_chai), which is a side effect.
    global total_chai
    total_chai += x
    return total_chai

# Recursive Function Example--------------
# Function is doing to call itself until the termination condition is met.
def pour_chai(n):
    if n == 0:
        print("All cups are poured!")
        return # early exit/termination condition
    print(f"Pouring cup {n}...") 
    pour_chai(n - 1)  # Recursive call with decremented n
    
pour_chai(5)  # Start pouring 5 cups of chai

# Lambda Function Example--------------
# A lambda functions is a small anonymous function defined with the lambda keyword.
# It can take any number of arguments but can only have one expression.
# Not reusable like normal functions.

chai_types = ["Masala Chai", "Cardamom Chai", "Ginger Chai", "Tulsi Chai", "Rose Chai" , "Masala Chai"]

strong_chai=list(filter(lambda chai: "Masala" not in chai, chai_types))
# Explaination: here we are using filter function to filter out the chai types which does not contain "Masala" in their name.
print("Strong Chai Types:", strong_chai)