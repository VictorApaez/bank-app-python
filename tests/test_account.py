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

def test_transactions():
    account = Account('123456', 100)
    account.deposit(50)
    account.withdraw(25)
    assert len(account.transactions) == 2

def test_transaction_logs():
    account = Account("123456789", 1000)

    account.deposit(500)
    account.withdraw(200)
    account.deposit(300)


    transaction_generator = account.transaction_logs()
    assert next(transaction_generator)[:2] == ("deposit", 500)
    assert next(transaction_generator)[:2] == ("withdraw", 200)
    assert next(transaction_generator)[:2] == ("deposit", 300)
        # ^^^ [:2] ignoring the last param which is the time stamp
    # Trying to fetch another transaction will raise StopIteration as the generator is exhausted
    # assert next(transaction_generator) # Uncomment this line to see the StopIteration error
