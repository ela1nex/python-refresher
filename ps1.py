class BankAccount:
    def __init__(self, balance, name, account_number):
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def withdraw(self, amount):
        """Withdraw money from the balance of an instance of BankAccount."""
        if (
            (type(amount) != int and type(amount) != float)
            or amount > self.balance
            or amount <= 0
        ):
            return False
        self.balance -= amount
        return True

    def deposit(self, amount):
        """Deposit money into the balance of an instance of BankAccount."""
        if (type(amount) != int and type(amount) != float) or amount <= 0:
            return False
        self.balance += amount
        return True

    def get_balance(self):
        """Print the balance of an instance of BankAccount."""
        print(f"current balance: {self.balance}")
        return self.balance
