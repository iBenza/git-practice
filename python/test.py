import unittest
import math

class MathTest(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(math.negative(5), -5)
        self.assertEqual(math.negative(0), 0)

    def test_power(self):
        self.assertEqual(math.power(2, 3), 8)
        self.assertEqual(math.power(5, 0), 1)

    def test_absolute(self):
        self.assertEqual(math.absolute(0), 0)
        self.assertEqual(math.absolute(10), 10)
        self.assertEqual(math.absolute(-10), -10)

    def test_is_even(self):
        self.assertEqual(math.is_even(0), True)
        self.assertEqual(math.is_even(5), False)
        self.assertEqual(math.is_even(-5), False)
        self.assertEqual(math.is_even(-10), True)
        self.assertEqual(math.is_even(10), True)

    def test_is_odd(self):
        self.assertEqual(math.is_odd(0), False)
        self.assertEqual(math.is_odd(5), True)
        self.assertEqual(math.is_odd(-5), True)
        self.assertEqual(math.is_odd(-10), False)
        self.assertEqual(math.is_odd(10), False)

if __name__ == "__main__":
    unittest.main()
