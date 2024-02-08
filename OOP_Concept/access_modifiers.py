class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"Hi myself {self.name} from Student class")
s1 = Student("Rahul")
s1.display()
        