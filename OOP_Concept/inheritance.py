class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"{self.brand} price is {self.price}")

class Sansang(Mobile):
    pass

Samsang_1 = Mobile("S24 Ultra", 240000)
Samsang_1.display()

Iphone_1 = Mobile("iphone 13", 125000)
Iphone_1.display()