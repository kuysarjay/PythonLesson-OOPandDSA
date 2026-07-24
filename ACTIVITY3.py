import math
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("===== CALCULATOR APP =====")

    num1 = float(input("Enter first number: "))

    print("\nChoose an operator")
    print("[+] Addition")
    print("[-] Subtraction")
    print("[*] Multiplication")
    print("[/] Division")
    print("[r] Square Root")
    print("[^] Power")
    print("[e] Exit")

    operator = input("Enter operator: ")

    if operator == "e":
        print("Thank you for using the calculator!")
        break

    if operator in ["+", "-", "*", "/", "^"]:
        num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Answer:", num1 + num2)

    elif operator == "-":
        print("Answer:", num1 - num2)

    elif operator == "*":
        print("Answer:", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Answer:", num1 / num2)
        else:
            print("Cannot divide by zero.")

    elif operator == "^":
        print("Answer:", math.pow(num1, num2))

    elif operator == "r":
        if num1 >= 0:
            print("Answer:", math.sqrt(num1))
        else:
            print("Square root is not defined for negative numbers.")

    else:
        print("Invalid operator!")

    input("\nPress Enter to continue...")