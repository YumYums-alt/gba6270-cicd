"""Unit tests for calculator.py. Jenkins runs these on every push."""
import unittest

from calculator import add, subtract, square, cube


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
      
    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_cube(self):
        self.assertEqual(cube(3), 27)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)


if __name__ == "__main__":
    unittest.main()
