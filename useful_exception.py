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
        
# Example code:
def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: wrong input")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
    return value;


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)