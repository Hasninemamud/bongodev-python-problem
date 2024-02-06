class Father:
    def __init__(self, f_name):
        self.f_name = f_name


class Mother:
    def __init__(self, m_name):
        self.m_name = m_name

class Child(Father, Mother):
    def __init__(self, f_name, m_name, name):
        super(Father).__init__(f_name)
        super(Mother).__init__(m_name)
        self.name = name

    def display(self):
        print(f"Father name is: {self.f_name}\nMother name is: {self.m_name}\nHis name is: {self.name}")

object_1 = Child("Abul", "Shahida", "Hemel")
object_1.set_age(30)  # Setting the age using the Father class method
object_1.display()



# class Human:
#     def eat(self):
#         print("I can eat")
#     def work(self):
#         print("I can work")

# class Male:
#     def flirt(self):
#         print("I can flirt")
#     def work(self):
#         print("I can code")

# class Boy(Human, Male):
#     pass

# boy_1 = Boy()
# boy_1.work()
# Male.work(boy_1)
