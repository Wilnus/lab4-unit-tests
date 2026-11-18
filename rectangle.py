import unittest

def area(a, b):
    '''
    Вычисляет площадь прямоугольника.

    Параметры:
        a (int, float): длина прямоугольника
        b (int, float): ширина прямоугольника

    Возвращаемое значение:
        (int, float): площадь прямоугольника

    Пример вызова:
        area(5, 3)
    '''
    return a * b 

def perimeter(a, b):
    '''
    Вычисляет периметр прямоугольника.

    Параметры:
        a (int, float): длина прямоугольника
        b (int, float): ширина прямоугольника

    Возвращаемое значение:
        (int, float): периметр прямоугольника

    Пример вызова:
        perimeter(5, 3)
    '''
    return (a + b)*2


class RectangleTestCase(unittest.TestCase):
    def test_zero_area_mul(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_zero_perimeter_mul(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(2, 5)
        self.assertEqual(res, 10)

    def test_perimeter_mul(self):
        res = perimeter(2, 5)
        self.assertEqual(res, 14)

    def test_float_area(self):
        res = area(2.5, 4)
        self.assertAlmostEqual(res, 10.0)
    
    def test_float_perimeter(self):
        res = perimeter(2.5, 3)
        self.assertAlmostEqual(res, 11.0)

    def test_one_zero_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_one_zero_perimeter(self):
        res = perimeter(5, 0)
        self.assertEqual(res, 10)

    def test_large_area(self):
        res = area(1000, 2000)
        self.assertEqual(res, 2000000)

    def test_large_perimeter(self):
        res = perimeter(1000, 2000)
        self.assertEqual(res, 6000)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -5, 10)

    def test_negative_area(self):
        self.assertRaises(ValueError, perimeter, -5, 10)
    