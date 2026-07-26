# Exception - An exception is an error that occurs while a program is running,
    # interrupting the normal flow of the program unless it is handled.
# The 'try' keyword begins a block of the code which may or may not be performing correctly;
    # next, Python tries to perform the risky action; if it fails,
    # an exception is raised and Python starts to look for a solution;
# The 'except' keyword starts a piece of code which will be executed if anything inside the try block goes wrong –
    # if an exception is raised inside a previous try block, it will fail here,
    # so the code located after the except keyword should provide an adequate reaction to the raised exception;
# returning to the previous nesting level ends the try-except section.

# Example of try-except function:

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")