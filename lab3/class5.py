class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. Current balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. Current balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")


account = BankAccount("John Doe", 1000)
account.deposit(500)  
account.withdraw(200)  
account.withdraw(1500)  
    