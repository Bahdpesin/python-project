# Simple Banking System

balance = 0  # starting balance
running = True

while running:
    print("\n===== Simple Banking System =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"\nYour current balance is: ₦{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₦"))
        if amount > 0:
            balance += amount
            print(f"₦{amount} deposited successfully!")
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₦"))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"₦{amount} withdrawn successfully!")
        elif amount > balance:
            print("Insufficient funds!")
        else:
            print("Invalid amount.")

    elif choice == "4":
        print("Thank you for using our banking system. Goodbye!")
        running = False

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")