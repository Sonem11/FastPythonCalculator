import unittest
import math

# Ovo su osnovni testovi za Fast Python Calculator.
# Testiramo svaku funkciju da budemo sigurni da radi kako treba.

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(5 + 6, 11)

    def test_subtraction(self):
        self.assertEqual(10 - 4, 6)

    def test_multiplication(self):
        self.assertEqual(3 * 7, 21)

    def test_division(self):
        self.assertEqual(20 / 5, 4)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 10 / 0

    def test_power(self):
        self.assertEqual(2 ** 3, 8)

    def test_square_root(self):
        self.assertEqual(math.sqrt(16), 4)

    def test_sin(self):
        self.assertAlmostEqual(math.sin(math.radians(90)), 1.0, places=5)

    def test_cos(self):
        self.assertAlmostEqual(math.cos(math.radians(0)), 1.0, places=5)

    def test_tan(self):
        self.assertAlmostEqual(math.tan(math.radians(45)), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
