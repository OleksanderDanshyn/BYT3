import math
from abc import ABC, abstractmethod


class IShape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_volume(self):
        pass


class Sphere(IShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 4 * math.pi * self.radius ** 2

    def calculate_volume(self):
        return (4.0 / 3.0) * math.pi * self.radius ** 3


class Cylinder(IShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def calculate_volume(self):
        return math.pi * self.radius ** 2 * self.height


class Rectangle(IShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_volume(self):
        return 0


class Cube(IShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return 6 * self.side ** 2

    def calculate_volume(self):
        return self.side ** 3


if __name__ == "__main__":
    sphere = Sphere(5)
    print("Sphere:")
    print(f"Area: {sphere.calculate_area():.3f}")
    print(f"Volume: {sphere.calculate_volume():.3f}")
    print()

    cylinder = Cylinder(3, 7)
    print("Cylinder:")
    print(f"Area: {cylinder.calculate_area():.3f}")
    print(f"Volume: {cylinder.calculate_volume():.3f}")
    print()

    rectangle = Rectangle(4, 8)
    print("Rectangle:")
    print(f"Area: {rectangle.calculate_area():.3f}")
    print(f"Volume: {rectangle.calculate_volume():.3f}")
    print()

    cube = Cube(4)
    print("Cube:")
    print(f"Area: {cube.calculate_area():.3f}")
    print(f"Volume: {cube.calculate_volume():.3f}")