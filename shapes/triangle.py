try:
    from .base import Shape
except ImportError:
    from base import Shape
import math

class Triangle(Shape):
    """Класс для представления треугольника"""
    
    def __init__(self, side_a: float, side_b: float, side_c: float):
        # Проверка валидности сторон
        sides = [side_a, side_b, side_c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть положительными числами")
        
        # Проверка неравенства треугольника
        if max(sides) > sum(sides) - max(sides):
            raise ValueError("Треугольник с такими сторонами не существует")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self) -> float:
        """Вычисляет площадь треугольника по формуле Герона"""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self) -> float:
        """Вычисляет периметр треугольника"""
        return self.side_a + self.side_b + self.side_c
    
    def is_right_triangle(self) -> bool:
        """Проверяет, является ли треугольник прямоугольным"""
        sides = sorted([self.side_a, self.side_b, self.side_c])
        # Используем встроенную функцию math.isclose()
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
    
    def __str__(self) -> str:
        return f"Треугольник (стороны={self.side_a}, {self.side_b}, {self.side_c})"