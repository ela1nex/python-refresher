class BankAccount:
    def __init__(self, balance, name, account_number):
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def get_balance(self):
        return self.balance
