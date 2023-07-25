from bank import Bank
from account import Account
from customer import Customer

def test_customer_creation():
    bank = Bank('Test Bank')
    customer = Customer('John Doe', '123 Main St', bank)
    assert customer.name == 'John Doe'
    assert customer.address == '123 Main St'
    assert len(customer.accounts) == 0

def test_open_account():
    bank = Bank('Test Bank')
    customer = Customer('John Doe', '123 Main St', bank)
    account = customer.open_account('123456', 100)
    assert len(customer.accounts) == 1
    assert isinstance(account, Account)
    assert account in customer.accounts

def test_close_account():
    bank = Bank('Test Bank')
    customer = Customer('John Doe', '123 Main St', bank)
    account = customer.open_account('123456', 100)
    account.withdraw(100)
    customer.close_account('123456')
    assert len(customer.accounts) == 0

def test_transfer_money():
    bank = Bank('Test Bank')
    customer = Customer('John Doe', '123 Main St', bank)
    account1 = customer.open_account('123456', 100)
    account2 = customer.open_account('789012', 50)
    customer.transfer_money('123456', '789012', 50)
    assert account1.balance == 50
    assert account2.balance == 100
