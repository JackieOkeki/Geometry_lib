import unittest
import math
import sys
import os

# Добавляем родительскую директорию в путь Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Абсолютный импорт
from shapes.circle import Circle

from init import calculate_area

class TestCircle(unittest.TestCase):
    
    def test_area_calculation(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)
    
    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            Circle(0)
    
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
    
    def test_calculate_area_function(self):
        circle = Circle(3)
        area = calculate_area(circle)
        self.assertAlmostEqual(area, math.pi * 9)

if __name__ == '__main__':
    unittest.main()