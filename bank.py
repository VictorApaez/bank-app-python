from account import Account
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    
    def create_account(self, account_number, initial_balance = 0):
        for account in self.accounts:
            if (account.account_number == account_number):
                raise ValueError("Account number already exists!")
        new_account = Account(account_number, initial_balance)
        self.accounts.append(new_account)
        return new_account
    
    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                if account.balance != 0:
                    raise ValueError("Cannot delete account with a non-zero balance.")
                self.accounts.remove(account)
                return
        raise ValueError("Account not found.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise ValueError("Account not found.")