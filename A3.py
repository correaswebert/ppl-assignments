class Shape(object):
    """abstract class"""
    edges = None                            # public variable
    __secret = "this is a secret value"     # private variable

    def __str__(self):
        return f"I am a {self.edges}-sided shape!"

    def get_secret(self):
        return self.__secret


class Triangle(Shape):
    def __init__(self):
        """initialize object when called"""
        self.edges = 3


class EquilateralTriangle(Triangle):
    def __init__(self):
        super().__init__()
        self.angle = 60

    def __str__(self):
        return super().__str__() + f"\nI also have all angles equal to {self.angle}."


class IsocelesTriangle(Triangle):
    def __str__(self):
        return super().__str__() + "\nI also have two equal sides!"


class Quadrilateral(Shape):
    def __init__(self):
        self.edges = 4


class Parallelogram(Quadrilateral):
    def __str__(self):
        return super().__str__() + "\nI also have opposite sides parallel!"


class Rectangle(Parallelogram):
    def __str__(self):
        return super().__str__() + "\nI also have opposite sides equal!"


class Rhombus(Parallelogram):
    def __str__(self):
        return super().__str__() + "\nI also have all sides equal!"


class Square(Rhombus, Rectangle):
    """order of execution goes from RTL"""

    def get_secret(self):
        try:
            print(self.__secret)
        except:
            print("Cannot access private variable!")


class Circle(Shape):
    def __init__(self):
        self.edges = float("inf")

    def __str__(self):
        "I have infinitely many sides!"


if __name__ == "__main__":
    t = EquilateralTriangle()
    print(t)
    print()

    s = Square()
    print(s)
    print()

    print(t.get_secret())
    print(s.get_secret())
