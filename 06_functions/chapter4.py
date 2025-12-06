# Non Local vs Global Scope
# Non-local scope refers to variables defined in the nearest enclosing function that is not global.
# Gobal scope refers to variables defined at the top level of a module or script.
# Many developers avoid using global scope to prevent unintended side effects across different parts of the code.

#NON LOCAL SCOPE EXAMPLE ---------------------------
print("\n--- Non-Local Scope Example ---")
def update_order():
    chai_type="Elaichi Chai" # local scope
    print(f"Initial order: {chai_type}")
    def kitchen():
        #  use of nonlocal keyword to modify chai_type from the enclosing scope
        nonlocal chai_type  # referring to the nearest enclosing scope variable
        chai_type="Kesar Chai" # modifying non-local variable
        print(f"Kitchen prepared: {chai_type}")
    kitchen()
    print(f"Order served: {chai_type}") # reflects change made in kitchen()

update_order()

# GLOBAL SCOPE EXAMPLE -------------------------------
print("\n--- Global Scope Example ---")
chai_type="Masala Chai" # global scope
print(f"Initial global chai type: {chai_type}")
def front_desk():
    def kitchen():
        global chai_type  # referring to the global variable
        chai_type="Ginger Chai" # modifying global variable
        print(f"Kitchen prepared: {chai_type}")
    kitchen()
    print(f"Order served: {chai_type}") # reflects change made in kitchen()
front_desk()
print(f"Final chai type globally: {chai_type}") # reflects change made in kitchen()