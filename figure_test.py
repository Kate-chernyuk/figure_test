import math
from abc import ABC, abstractmethod
import unittest

class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        return 0.0
    

class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        if self.radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        if any(side <= 0 for side in [self.a, self.b, self.c]):
            raise ValueError("Стороны треугольника должны быть положительными")
        if not self.is_triangle():
            raise ValueError("Указанные стороны не могут образовать треугольник")
        
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return sides[0]**2 + sides[1]**2 == sides[2]**2

    def is_triangle(self) -> bool:
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a


def calculate_area(figure: Figure) -> float:
    return figure.area()


class TestFigure(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 5 ** 2)

        with self.assertRaises(ValueError):
            Circle(-1).area()

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

        with self.assertRaises(ValueError):
            Triangle(1, 1, 3).area()  

        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5).area()

    def test_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle2 = Triangle(2, 2, 3)
        self.assertFalse(triangle2.is_right_triangle())

    def test_is_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_triangle())
        self.assertFalse(Triangle(1, 1, 3).is_triangle())


if __name__ == "__main__":
    unittest.main()
