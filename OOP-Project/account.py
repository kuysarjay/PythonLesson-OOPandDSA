from datetime import datetime


# ==========================================
# Parent Class (Inheritance)
# ==========================================
class Account:

    # Constructor
    def __init__(self, account_number, owner, balance=0):

        # Encapsulation
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transactions = []

    # Method
    def deposit(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        self.balance += amount

        date = datetime.now().strftime("%B %d, %Y | %I:%M:%S %p")

        self.transactions.append(
            f"{date} | Deposit | +${amount:.2f}"
        )

        print("\nDeposit Successful!")
        print("Transaction Date:", date)
        print(f"Current Balance: ${self.balance:.2f}")

    # Method
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")

        elif amount > self.balance:
            print("Insufficient Balance.")

        else:

            self.balance -= amount

            date = datetime.now().strftime("%B %d, %Y | %I:%M:%S %p")

            self.transactions.append(
                f"{date} | Withdraw | -${amount:.2f}"
            )

            print("\nWithdrawal Successful!")
            print("Transaction Date:", date)
            print(f"Remaining Balance: ${self.balance:.2f}")

    # Method
    def display_balance(self):

        date = datetime.now().strftime("%B %d, %Y | %I:%M:%S %p")

        print("\n========== ACCOUNT ==========")
        print("Transaction Date:", date)
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.owner}")
        print(f"Balance         : ${self.balance:.2f}")

    # Method
    def get_transactions(self):
        return self.transactions

    # Polymorphism
    # This method will be overridden by the child class.
    def account_type(self):
        return "Regular Account"


# ==========================================
# Child Class (Inheritance)
# ==========================================
class SavingsAccount(Account):

    # Constructor
    def __init__(self, account_number, owner, balance=0):

        # Calls the parent constructor
        super().__init__(account_number, owner, balance)

    # Method Overriding (Polymorphism)
    def account_type(self):
        return "Savings Account"

    # Additional Method
    def add_interest(self):

        interest = self.balance * 0.02

        self.balance += interest

        date = datetime.now().strftime("%B %d, %Y | %I:%M:%S %p")

        self.transactions.append(
            f"{date} | Interest | +${interest:.2f}"
        )

        print("\nInterest Added Successfully!")
        print(f"Interest Earned : ${interest:.2f}")
        print(f"New Balance     : ${self.balance:.2f}")