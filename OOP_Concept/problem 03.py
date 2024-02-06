class Bank_Account:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"Successfully deposited ${amount}. New balance: ${self.balance}")
        

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        print(f"Withdraw ${withdraw_amount}. New balance ${self.balance}")


    def display(self):
        return self.balance
    
account_1 = Bank_Account("Akash", 1000)
account_1.deposite(500)
account_1.withdraw(200)

current_balance = account_1.display()
print(f"Current balance for {account_1.name} is ${account_1.balance}")

