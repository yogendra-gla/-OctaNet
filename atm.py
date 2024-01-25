class BankAccount:
    def __init__(self, balance=0, transaction_history=[]):
        self.balance = balance
        self.transaction_history = transaction_history

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal failed.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")

    def transfer(self, amount, recipient_account):
        if amount > self.balance:
            print("Insufficient funds! Transfer failed.")
        else:
            self.balance -= amount
            recipient_account.deposit(amount)
            self.transaction_history.append(f"Transferred ${amount} to {recipient_account}")

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    account1 = BankAccount()
    account2 = BankAccount()

    while True:
        print("\nATM Interface")
        print("1. Transaction History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account1.display_transaction_history()
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: $"))
            account1.withdraw(amount)
        elif choice == '3':
            amount = float(input("Enter deposit amount: $"))
            account1.deposit(amount)
        elif choice == '4':
            amount = float(input("Enter transfer amount: $"))
            account1.transfer(amount, account2)
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
