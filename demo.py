
"""
Демонстрационный скрипт для работы с библиотекой
"""


# Добавляем текущую директорию в путь Python
#sys.path.insert(0, os.path.dirname(__file__))

from init import calculate_area
from shapes.circle import Circle
from shapes.triangle import Triangle

def main():
    print("Демонстрация работы библиотеки:")
    print("=" * 40)
    
    # Круг
    circle = Circle(5)
    print(f"Круг с радиусом 5: площадь = {circle.area():.2f}")
    
    # Треугольник
    triangle = Triangle(3, 4, 5)
    print(f"Треугольник 3-4-5: площадь = {triangle.area():.2f}")
    print(f"Прямоугольный? {triangle.is_right_triangle()}")
    
    # Универсальная функция
    print(f"Универсальный расчет площади круга: {calculate_area(circle):.2f}")
    print(f"Универсальный расчет площади треугольника: {calculate_area(triangle):.2f}")

if __name__ == "__main__":
    main()