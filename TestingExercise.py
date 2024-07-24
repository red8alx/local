#Exercise 1: Understanding the Importance of Testing
import unittest
def cal_sqaure_value (num):
    sqr_value = num + num
    return sqr_value
class TestCalSquareValue(unittest.TestCase):
    def test_result(self):
        result = cal_sqaure_value(-6)
        self.assertEqual(result, 12)
if __name__ == "__main__":
  unittest.main()