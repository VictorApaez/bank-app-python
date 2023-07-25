def log_transaction(func):
    def wrapper(account, amount):
        print(f"Transaction: {func.__name__} {amount}")
        return func(account, amount)
    return wrapper

def validate_transaction(func):
    def wrapper(account, amount):
        if amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        if func.__name__ == 'withdraw' and amount > account.balance:
            raise ValueError("Insufficient funds!")
        return func(account, amount)
    return wrapper
