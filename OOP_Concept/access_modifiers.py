class Student:
    def __init__(self,name, rollnum,age):
        self.name = name
        self._rollnum = rollnum #protected instance
        self.__age = age
        
    def __display(self):
        print(f"Hi myself {self.name} from Student class")
class Branch(Student):
    pass

s1 = Branch("Rahul", 22, 15)
print(s1.name)
print(s1._rollnum)
print(s1.__age)
        