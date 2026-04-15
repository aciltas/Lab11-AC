import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 1), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(7, -3), 4)

     def test_subtract(self):
         self.assertEqual(subtract(12, 2), 10)
         self.assertEqual(subtract(1, 1), 0)
         self.assertEqual(subtract(-6, -2), -4)

    def test_multiply(self):
        self.assertEqual(multiply(8, 8), 64)
        self.assertEqual(multiply(3, 0), 0)
        self.assertEqual(multiply(-2, -2), 4)
        
        
    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(-10, 5), -2)
        self.assertEqual(divide(3, 0), 0)


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithim(16, 2), 4)
        self.assertAlmostEqual(logarithim(100, 10), 2)
        self.assertAlmostEqual(logarithim(8, 2), 3)


    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithim(5, 1)
                       
    
    def test_log_invalid_argument(self): 
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): 
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)
        self.assertAlmostEqual(hypotenuse(3, 4), 5)


    def test_sqrt(self): 
        with self.assertRaises(ValueError):
            square_root(-1)
   
# Do not touch this
if __name__ == "__main__":
    unittest.main()
