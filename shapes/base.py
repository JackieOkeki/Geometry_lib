from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Абстрактный базовый класс для всех фигур"""
    
    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление фигуры"""
        pass