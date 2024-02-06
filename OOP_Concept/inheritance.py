class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def realese_date(self, date):
        self.date = date

    def display(self):
        print(f"{self.brand} price is {self.price} & Realese date {self.date}")

class Sansang(Mobile):
    pass

class Iphone(Mobile):
    pass

Samsang_1 = Sansang("Samsang S24 Ultra", 240000)
Samsang_1.realese_date("12 March")
Samsang_1.display()

Iphone_1 = Mobile("iphone 13", 125000)
Iphone_1.realese_date("15 March")
Iphone_1.display()