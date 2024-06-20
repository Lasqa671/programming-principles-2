"""
Create a bank account class that has 
attributes owner, balance and two methods 
deposit and withdraw. Withdrawals may not 
exceed the available balance. 
Instantiate your class, make several deposits 
and withdrawals, and test to make sure the 
account can't be overdrawn.
"""
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
            else:
                print("Insufficient funds. Withdrawal not accepted")
        else:
            print("Invalid withdrawal amount. Please enter positive value.")

account = Account("Bob Ross", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800)
account.deposit(1000)
account.withdraw(1200)