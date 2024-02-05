class Vahicle:

    def __init__(self, name, milege, capacity, ):
        self.name = name
        self.milege = milege
        self.capacuty = capacity
        self.colour = "white"
    
    def display(self):
        print(f"{self.name} milege is {self.milege} and capacity is {self.capacuty} also {self.colour} colour")

Bus = Vahicle("Toyota", 7.80, 10 )
Bus.display()

Honda = Vahicle("R15", 100.30, 2)
Honda.display()