class Animal(object):
    """this is a abstract class as all the methods are abstract
    hence it is an interface as derived classes must implement these mothods"""

    def __init__(self):
        """abstract (virtual) method is meant to be strictly implemented
        in the derived class, but does not provied any basic functionality"""
        raise NotImplementedError


class Mammal(Animal):
    def __init__(self):
        self.species = self.__class__.__name__


class Bird(Animal):
    def __init__(self):
        self.species = self.__class__.__name__


class Reptile(Animal):
    def __init__(self):
        self.species = self.__class__.__name__


class Amphibian(Animal):
    def __init__(self):
        self.species = self.__class__.__name__


class Fish(Animal):
    def __init__(self):
        self.species = self.__class__.__name__


class Eagle(Bird):
    def feature(self):
        return "I am the national symbol of the USA."


class Platypus(Amphibian):
    pass


class Human(Mammal):
    # thus it is an example of polymorphism
    def __init__(self, name):
        super().__init__()      # error if we remove this line
        self.name = name

    def __str__(self):
        return f"My name is {self.name}. I am {self.species}."


class ElonMusk(Human):
    """Animal -> Human -> ElonMusk"""

    # polymorphism -> base class method is overridden in
    # derived class with the same name

    def __init__(self):
        self.species = "SuperHuman"

    def __str__(self):
        return "I am Super-Human Elon Musk"


if __name__ == "__main__":
    h = Human("Swebert")
    print(h)
    e = ElonMusk()
    print(e)
