from bank import Bank
from account import Account

def test_bank_creation():
    bank = Bank('Test Bank')
    assert bank.name == 'Test Bank'
    assert len(bank.accounts) == 0

def test_account_creation():
    bank = Bank('Test Bank')
    bank.create_account('123456', 100)
    assert len(bank.accounts) == 1
    assert bank.accounts[0].account_number == '123456'
    assert bank.accounts[0].balance == 100

def test_account_retrieval():
    bank = Bank('Test Bank')
    bank.create_account('123456', 100)
    account = bank.find_account('123456')
    assert isinstance(account, Account)
    assert account.account_number == '123456'

def test_account_deletion():
    bank = Bank('Test Bank')
    account = bank.create_account('123456', 100)
    account.withdraw(100) # cannot delete account with a balance
    bank.delete_account('123456')
    assert len(bank.accounts) == 0
