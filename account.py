import datetime

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transactions.append(('deposit', amount, currentTime))
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")
        self.balance -= amount
        currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transactions.append(('deposit', amount, currentTime))
        return self.balance