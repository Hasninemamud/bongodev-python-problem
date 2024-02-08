from abc import ABC, abstractmethod
class Area(ABC):
    @abstractmethod
    def cal(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

     
class Triangle(Area):
    def __init__(self):
        Triangle.__init__(self, dim1, dim2):
        
    
    def result(self,):
        t_area = 0.5 * self.dim1 * self.dim2
        print(f"{t_area}")

t1 = Triangle(10,20)
t1.result()
