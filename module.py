# A module is a Python (.py) file that contains reusable code,
    # such as functions, classes, variables, and statements.
# A module is a Python file that contains reusable code and can
    # be imported into another Python program using the import statement.

# Why use modules?
# - Reuse code
# - Organize programs
# - Make code easier to maintain
# - Access built-in and third-party libraries

# Types of Modules:

# 1. Built-in Modules
    # Included with Python
    # Examples: math, random, os, datetime, sys

# 2. User-Defined Modules
    # Modules created by the programmer
    # Example: calculator.py

# 3. Third-Party Modules
    # Created by other developers
    # Installed using: pip install <module_name>
    # Examples: requests, numpy, pandas, matplotlib

# Ways to Import Modules:
# - import math
# - from math import sqrt
# - import math as m
# - from math import *   # Not recommended

# Example of Simple Calculator using the built-in math module
import math
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero."

    def square_root(self, a):
        if a >= 0:
            return math.sqrt(a)
        return "Square root is not defined for negative numbers."