class Human:
    def __init__(self, eyes, nose):
        self.eyes = eyes
        self.nose = nose
        
    
class Men(Human):
    def __init__(self, salary):
        self.salary = salary
    def work(self):
        print(f"I work as a Software Engineer")

class Boy(Men):
    def __init__(self,eyes,nose,salary,car):
        Human.__init__(self, eyes, nose)
        Men.__init__(self, salary)
        self.car = car

    def work(self):
        print("I can code")

boy_1 = Boy(2, 1200, 1, 3)
print(boy_1.eyes)

