# A user-defined module is a Python (.py) file created by the programmer.
# It contains reusable code such as functions, classes, or variables
    # and can be imported into another Python program.
    
# Example of User-Define Module:
from module import Calculator

calc = Calculator()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root (first number)")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    print("Answer:", calc.add(num1, num2))

elif choice == "2":
    print("Answer:", calc.subtract(num1, num2))

elif choice == "3":
    print("Answer:", calc.multiply(num1, num2))

elif choice == "4":
    print("Answer:", calc.divide(num1, num2))

elif choice == "5":
    print("Answer:", calc.square_root(num1))

else:
    print("Invalid choice.")