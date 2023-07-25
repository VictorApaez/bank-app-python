from account import Account

def main():
    # Create a new Account instance
    acc = Account('123456', 100)

    # Test deposit method
    acc.deposit(50)
    acc.deposit(10)

    # Test withdraw method
    acc.withdraw(7)

        
    # Attempt to withdraw more than the current balance
    try:
       acc.withdraw(500)
    except ValueError as e:
        print(e)
    
    print(f"Transaction History:")
    for transaction in acc.transactions:
        print(transaction)

if __name__ == "__main__":
    main()
