import unittest
import math
import sys
import os

# Добавляем родительскую директорию в путь Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Абсолютный импорт
from shapes.triangle import Triangle
from init import calculate_area

class TestTriangle(unittest.TestCase):
    
    def test_area_calculation(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)
    
    def test_right_triangle_detection(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())
        
        triangle2 = Triangle(5, 6, 7)
        self.assertFalse(triangle2.is_right_triangle())
    
    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)
    
    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)
    
    def test_calculate_area_function(self):
        triangle = Triangle(3, 4, 5)
        area = calculate_area(triangle)
        self.assertAlmostEqual(area, 6.0)

if __name__ == '__main__':
    unittest.main()