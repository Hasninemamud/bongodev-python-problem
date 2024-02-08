class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        return area

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        return area

    def display(self):
        triangle_area = Triangle.area()  # Create a Triangle object and call its area()
        rectangle_area = self.area()

        print(f"Area is {triangle_area}")
        print(f"Area is {rectangle_area}")

# Create an object of the Rectangle class
obj_1 = Rectangle(12, 24)
obj_1.display()

# Create an object of the Triangle class
obj_2 = Triangle(10, 11)
obj_2.display()
