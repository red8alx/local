import unittest
import calc

class Test_calc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 20)
        self.assertEqual(result, 30)
    def test_subtract(self):
        result = calc.subtract(20, 7)
        self.assertEqual(result, 13)
    def test_multiply(self):
        result = calc.multiply(2, 4)
        self.assertEqual(result, 8)
    def test_divide(self):
        result = calc.divide(5, 1)
        self.assertEqual(result, 5)
        #self.assertRaises(ZeroDivisionError, calc.divide, 10, 1)

if __name__ == "__main__":
    unittest.main()