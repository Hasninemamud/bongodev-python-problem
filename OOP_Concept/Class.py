class mobile:
    brand = ""
    price = ""

phone1 = mobile()
phone1.brand = "Samsang"
phone1.price = 17000

print(f"Phone brand {phone1.brand} & price {phone1.price}")



phone2 = mobile()
phone2.brand = "iphone"
phone2.price = 17000

print(f"Phone brand {phone2.brand} & price {phone2.price}")


# class Cat:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
        
#     def sleep(self):
#         print(f"{self.name} is now sleeping")
#     def eat(self, iteam):
#         print(f"{self.name} is now eating")

# my_cat = ("Billu", 5)

# my_cat.eat("fish")



class Student:
    gpa = ""
    roll = ""

rahim = Student()
print(isinstance(rahim, Student))
rahim.roll = 101
rahim.gpa = 3.67
print(f"Roll:{rahim.roll} and GPA:{rahim.gpa}")

hemel = Student()
hemel.roll = 102
hemel.gpa = 4.00
print(f"Roll: {hemel.roll} and GPA: {hemel.gpa}")