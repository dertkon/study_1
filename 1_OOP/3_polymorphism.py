from math import pi


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        s = self.width * self.height
        return s

    def perimeter(self):
        p = 2 * self.width + 2 * self.height
        return p


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        s = pi * self.radius**2
        return s

    def perimeter(self):
        p = 2 * pi * self.radius
        return p


shapes = [Rectangle(100, 200), Circle(200)]

for shape in shapes:
    print(shape.area(), shape.perimeter())