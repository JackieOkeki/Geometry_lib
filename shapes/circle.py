try:
    # Попробовать относительный импорт (когда файл часть пакета)
    from .base import Shape
except ImportError:
    # Fallback: абсолютный импорт (когда файл запускается напрямую)
    from base import Shape
from math import pi

class Circle(Shape):
    """Класс для представления круга"""
    
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius
    
    def area(self) -> float:
        """Вычисляет площадь круга"""
        return pi * self.radius ** 2
    
    def __str__(self) -> str:
        return f"Круг (радиус={self.radius})"