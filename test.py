import unittest
import math

class MathTest(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(math.negative(5), -5)
        self.assertEqual(math.negative(0), 0)

    def test_power(self):
        self.assertEqual(math.power(2, 3), 8)
        self.assertEqual(math.power(5, 0), 1)

if __name__ == "__main__":
    unittest.main()
