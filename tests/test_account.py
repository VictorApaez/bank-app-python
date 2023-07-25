from account import Account

def test_account_creation():
    account = Account('123456', 100)
    assert account.account_number == '123456'
    assert account.balance == 100

def test_deposit():
    account = Account('123456', 100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw():
    account = Account('123456', 100)
    account.withdraw(50)
    assert account.balance == 50

def test_insufficient_balance():
    account = Account('123456', 100)
    try:
        account.withdraw(200)
    except ValueError as e:
        assert str(e) == "Insufficient balance!"

def test_transaction_history():
    account = Account('123456', 100)
    account.deposit(50)
    account.withdraw(25)
    assert len(account.transactions) == 2
