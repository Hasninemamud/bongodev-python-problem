# Python is a versatile programming language that supports various programming styles, including object-oriented programming (OOP) through the use of objects and classes.

# An object is any entity that has attributes and behaviors. For example, a parrot is an object. It has

# attributes - name, age, color, etc.
# behavior - dancing, singing, etc.
# Similarly, a class is a blueprint for that object.

class Parrot:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def display(self):
        print(f"{self.name} is {self.age} years old")
    
parrot1 = Parrot("Hemel", 12)
parrot1.display()

