# class Instractor:
#     def __init__(self, instractor_name, insytacyor_add):
#         self.name = instractor_name
#         self.add = insytacyor_add

# instractir_1 = Instractor("Aman", "Bhola")
# print(instractir_1.name, instractir_1.add)

# class Phone:
#     def __init__(self, name, model, sold):
#         self.name = name
#         self.model = model
#         self.sold = 0
# mobile = Phone("Samsang", "S24", "100102")
# print(mobile.sold, mobile.model, mobile.name)
    
# class Tringle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def calculate_area(self):
#         area = 0.5 * self.base * self.height
#         print(f"Area {area}")

# t1 = Tringle(10, 20)
# t1.calculate_area()

class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Constructor to initialize account details
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Method to deposit money into the account
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        # Method to retrieve the current balance
        return self.balance

# Example usage of the BankAccount class
account1 = BankAccount("John Doe", 1000)

# Deposit money into the account
account1.deposit(500)

# Withdraw money from the account
account1.withdraw(200)

# Get the current balance
current_balance = account1.get_balance()
print(f"Current balance for {account1.account_holder}: ${current_balance}")



# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def calculate_area(self):
#         area = 0.5 * self.base * self.height
#         print(f"Area = {area}")
# t1 = Triangle(10, 20)
# t1.calculate_area()