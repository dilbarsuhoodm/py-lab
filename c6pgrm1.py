class BankAccount:
    def __init__(self, name, account_number, account_type, balance=0):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount should be positive.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_account_details(self):
        print("Account Details:")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

# Example usage:
account = BankAccount(name="John Doe", account_number="12345678", account_type="Savings", balance=1000)
account.display_account_details()
account.deposit(500)
account.withdraw(200)
account.display_account_details()

