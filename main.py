from account import Account

def main():
    # Create a new Account instance
    acc = Account('123456', 100)  # an account with account number '123456' and an initial balance of 100

    # Test deposit method
    print(f"Balance after depositing 50: {acc.deposit(50)}")
    print(f"Balance after depositing 50: {acc.deposit(10)}")

    # Test withdraw method
    print(f"Balance after withdrawing 70: {acc.withdraw(70)}")

    # Attempt to withdraw more than the current balance
    try:
        print(f"Attempting to withdraw 500: {acc.withdraw(500)}")
    except ValueError as e:
        print(e)
    
    print(f"Transaction History:")
    for transaction in acc.transactions:
        print(transaction)

if __name__ == "__main__":
    main()
