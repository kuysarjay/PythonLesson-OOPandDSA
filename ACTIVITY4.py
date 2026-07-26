print("=== Simple Calculator ===")

while True:
    print("\nChoose an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer:", num1 + num2)

        elif choice == "2":
            print("Answer:", num1 - num2)

        elif choice == "3":
            print("Answer:", num1 * num2)

        elif choice == "4":
            print("Answer:", num1 / num2)

        else:
            print("Invalid choice. Please select 1-5.")

    except ValueError:
        print("Error: Please enter valid numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")