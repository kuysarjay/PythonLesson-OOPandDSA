# ==========================================
# Transaction Class
# ==========================================
class Transaction:

    # Static Method
    @staticmethod
    def show_history(account):

        print("\n===================================")
        print("      TRANSACTION HISTORY")
        print("===================================")

        # Encapsulation
        # Access the transactions using the getter method.
        transactions = account.get_transactions()

        if len(transactions) == 0:
            print("No transactions found.")

        else:

            # Iteration
            for number, transaction in enumerate(transactions, start=1):
                print(f"{number}. {transaction}")

        print("===================================")