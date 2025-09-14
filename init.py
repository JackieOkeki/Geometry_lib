from shapes.circle import Circle
from shapes.triangle import Triangle

def calculate_area(Shape) -> float:
    """
    Вычисляет площадь фигуры без знания типа в compile-time
    
    Args:
        shape: Объект фигуры, наследуемый от Shape
    
    Returns:
        float: Площадь фигуры
    
    Raises:
        TypeError: Если переданный объект не является фигурой
    """
    if not hasattr(Shape, 'area') or not callable(getattr(Shape, 'area')):
        raise TypeError("Объект должен иметь метод area()")
    
    return Shape.area()

# Экспорт основных классов
__all__ = ['Circle', 'Triangle', 'calculate_area']