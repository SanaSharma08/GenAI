# Python Imports, Modules and init Files - Chapter 9
# We need import statements to use functions, classes, and variables defined in other files or modules.
# Modules help organize code into separate files, making it easier to manage and reuse.
# An __init__.py file indicates that a directory is a Python package, allowing us to import modules from it.


# 4 ways of importing modules: -----------------------------------------
# 1. Importing the entire module -----
# import masala_chai.py | use : masala_chai.brew_masala_chai() 
# 2. Importing specific functions or classes from a module ----
# from masala_chai.py import brew_masala_chai, prepare_chai | use : brew_masala_chai()
# 3. Importing all functions and classes from a module (not recommended for large modules) ----
# from masala_chai.py import * | use : brew_masala_chai()
# 4. Importing with an alias ------
# import masala_chai.py as mc | use : mc.brew_masala_chai()


# ----------------------------------------------------

# Somtimes, we may not import modules from external files, but from python standard library or installed packages.
# Example: Importing the math module from Python's standard library
import math
# Using the sqrt function from the math module
number = 16
sqrt_number = math.sqrt(number)