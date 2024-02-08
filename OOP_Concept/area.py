class Shape:
    # create a contructor
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    
class Tringle(Shape):
    def area(self, t_area):
        self.t_area = t_area
        t_area = 0.5 * self.height * self.width
        return t_area

class Recteangle(Shape):
    def area(self):
        r_area = self.height * self.width
        return r_area

    def display(self):
        print(f"Area is {self.t_area}")

area_1 = Tringle(12, 24)
area_1.display()
