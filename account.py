import datetime
from decorators import validate_transaction

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

    @validate_transaction
    def withdraw(self, amount):
        self.balance -= amount
        currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transactions.append(('withdraw', amount, currentTime))
        return self.balance
    
    def transaction_logs(self):
        for transaction in self.transactions:
            yield transaction