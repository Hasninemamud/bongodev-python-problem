# class Vahicle:

#     def __init__(self, name, milege, capacity, ):
#         self.name = name
#         self.milege = milege
#         self.capacuty = capacity
        
    
#     def display(self, company):
#         print(f"{self.name} milege is {self.milege} and capacity is {self.capacuty} also  {company}")

# Bus = Vahicle("Toyota", 7.80, 10 )
# Bus.display()

# Honda = Vahicle("R15", 100.30, 2)
# Honda.display("Olloy")


class Circle:
    pi = 3.1416
    
    def __init__(self, redius):
        self.redius = redius

    def circumstance(self):
        circums = 2 * self.pi * self.redius
        print(f"The circumstance is {circums}")

circle_1 = Circle(4)
circle_1.circumstance()
        



