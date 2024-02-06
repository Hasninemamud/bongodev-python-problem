# Write a Python program to create a person class. Include attributes like name, country and date of birth. 
#Implement a method to determine the person's age.
from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    
    def display(self):
        age = self.calculate_age()
        print(f"Person Name: {self.name}\nCountry: {self.country}\nAge: {age}")

# Creating an object of the Person class
person_1 = Person("Hemel", "Bangladesh", date(2000, 9, 21))
person_1.display()

