class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

#Taking inputs

name = input("Enter your name: ")
initial_balance = float(input("Enter starting balance: "))

acc = BankAccount(name, initial_balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        acc.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        acc.withdraw(amount)
    elif choice == "3":
        acc.check_balance()
    elif choice == "4":
        print(f"Thanks for using our bank, {name}")
        break
    else:
        print("Invalid choice.")