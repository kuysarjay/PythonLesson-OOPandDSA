# 1. Some abstract built-in Python exceptions are:
    # ArithmeticError
        # Raised for errors related to arithmetic operations (base class for arithmetic exceptions).
    # BaseException
        # The base class for all built-in exceptions in Python.
    # LookupError
        # Raised when a key or index used to access a collection is invalid.

# 2. Some concrete built-in Python exceptions are:
    # AssertionError
        # Raised when an assert statement fails.
    # ImportError
        # Raised when Python cannot import a module or object.
    # IndexError
        # Raised when trying to access a list, tuple, or string with an invalid index.
    # KeyboardInterrupt
        # Raised when the user interrupts the program, usually by pressing Ctrl + C.
    # KeyError
        # Raised when a dictionary key does not exist.
    # MemoryError
        # Raised when the program runs out of available memory.
    # OverflowError
        # Raised when the result of a calculation is too large to be represented.
        
# ArithmeticError
try:
    raise ArithmeticError("Arithmetic error occurred")
except ArithmeticError as e:
    print(e)
    
# BaseException
try:
    raise BaseException("Base exception occurred")
except BaseException as e:
    print(e)
    
# LookupError
try:
    raise LookupError("Lookup error occurred")
except LookupError as e:
    print(e)
    
# AssertionError
try:
    assert 5 > 10
except AssertionError:
    print("Assertion failed!")
    
# ImportError
try:
    import not_existing_module
except ImportError:
    print("Module not found!")
    
# IndexError
numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Index out of range!")
    
# KeyboardInterrupt
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted by user.")
    
# KeyError
student = {"name": "Nelson"}

try:
    print(student["age"])
except KeyError:
    print("Key does not exist!")
    
# MemoryError
try:
    x = []
    while True:
        x.append("Python")
except MemoryError:
    print("Out of memory!")
    
# OverflowError
import math

try:
    print(math.exp(1000))
except OverflowError:
    print("Number too large!")