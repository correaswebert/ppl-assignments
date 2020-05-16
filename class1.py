class Shape(object):
    """abstract class"""
    edges = None

    def __str__(self):
        return f"I am a {self.edges}-sided shape!"


class Triangle(Shape):
    def __init__(self):
        """initialize object when called"""
        self.edges = 3


class EquilateralTriangle(Triangle):
    def __init__(self):
        super().__init__()
        self.angle = 60

    def __str__(self):
        return super().__str__() + \
            f"\nI also have all angles equal to {self.angle}."


class IsocelesTriangle(Triangle):
    pass


class Parallelogram(Shape):
    pass


class Rectangle(Parallelogram):
    pass


class Rhombus(Parallelogram):
    pass


class Square(Rectangle, Rhombus):
    pass


class Trapezium(Shape):
    pass


class Circle(Shape):
    pass


t = IsocelesTriangle()
print(t)
