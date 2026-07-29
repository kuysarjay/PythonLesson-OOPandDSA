import os

from account import SavingsAccount
from transaction import Transaction

# ==========================================
# Object Creation
# ==========================================

# Your personal bank account
account = SavingsAccount(
    account_number="20260001",
    owner="Nelson",
    balance=10000
)

while True:

    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 45)
    print("         MY BANK ACCOUNT")
    print("=" * 45)
    print(f"Welcome, {account.owner}!")
    print("=" * 45)

    print("[1] Deposit")
    print("[2] Withdraw")
    print("[3] Check Balance")
    print("[4] Add Interest")
    print("[5] Transaction History")
    print("[6] Exit")

    choice = input("\nEnter your choice: ")

    try:

        if choice == "1":

            amount = float(input("Enter Deposit Amount: ₱"))
            account.deposit(amount)

        elif choice == "2":

            amount = float(input("Enter Withdrawal Amount: ₱"))
            account.withdraw(amount)

        elif choice == "3":

            account.display_balance()

        elif choice == "4":

            account.add_interest()

        elif choice == "5":

            Transaction.show_history(account)

        elif choice == "6":

            print("\nThank you for using My Bank Account!")
            break

        else:

            print("Invalid choice.")

    except ValueError:

        print("Invalid input. Please enter a valid number.")

    except KeyboardInterrupt:

        print("\nProgram interrupted.")
        break

    except Exception as e:

        print("Error:", e)

    input("\nPress Enter to continue...")