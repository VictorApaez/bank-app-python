from bank import Bank
class Customer:
    def __init__(self, name, address, bank):
        self.name = name
        self.address = address
        self.bank = bank
        self.accounts = []

    def open_account(self, account_number, initial_balance):
        account = self.bank.create_account(account_number, initial_balance)
        self.accounts.append(account)
        return account

    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.bank.delete_account(account_number)
                self.accounts.remove(account)
                break
        else:
            raise ValueError(f"No account with number {account_number} found.")

    def transfer_money(self, from_account_number, to_account_number, amount):
        from_account = self._find_account(from_account_number)
        to_account = self._find_account(to_account_number)

        from_account.withdraw(amount)
        to_account.deposit(amount)

    def _find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise ValueError(f"No account with number {account_number} found.")
