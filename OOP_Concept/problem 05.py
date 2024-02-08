# Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.
# math.pi * self.radius**2
# import math 
# class Circle:
#     pi = 3.1416

#     # create a constructor
#     def __init__(self, redius):
#         self.reduis = redius


    
#     def calculate_circle(self):
#         circle = self.pi * self.reduis ** 2
#         print(f"Circle are is {circle}")
    
        

# c_1 = Circle(4)
# c_1.calculate_circle()

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = input("Choose your option: ")

    def add(self):
        result = self.x + self.y
        print(f"Addition result: {result}")

    def sub(self):
        result = self.x - self.y
        print(f"Subtraction result: {result}")

    def multi(self):
        result = self.x * self.y
        print(f"Multiplication result: {result}")

    def divi(self):
        if self.y != 0:
            result = self.x / self.y
            print(f"Division result: {result}")
        else:
            print("Cannot divide by zero.")

cal_1 = Calculator(2, 3)

if cal_1.n == 'add':
    cal_1.add()
elif cal_1.n == 'sub':
    cal_1.sub()
elif cal_1.n == 'multi':
    cal_1.multi()
elif cal_1.n == 'divi':
    cal_1.divi()
else:
    print("Invalid option")

