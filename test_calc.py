import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    #Addition
    def test_addition_method_matches_calculate(self):
        calc = Calculator(7, 3, "+")
        self.assertEqual(calc.addition(), calc.calculate())

    def test_addition(self):
        self.assertEqual(Calculator(2, 2, "+").calculate(), 4)

    def test_addition_negative(self):
        self.assertEqual(Calculator(2, -2, "+").calculate(), 0)

    def test_addition_floats(self):
        self.assertAlmostEqual(Calculator(2.5, 3.7, "+").calculate(), 6.2, places=5)

    def test_addition_with_zero(self):
        self.assertEqual(Calculator(0, 5, "+").calculate(), 5)

    def test_addition_large_numbers(self):
        self.assertEqual(Calculator(1000000, 2000000, "+").calculate(), 3000000)


    #Subtruction
    def test_subtraction_method_matches_calculate(self):
        calc = Calculator(7, 3, "-")
        self.assertEqual(calc.subtraction(), calc.calculate())

    def test_subtraction(self):
        self.assertEqual(Calculator(2, 2, "-").calculate(), 0)

    def test_subtraction_negative(self):
        self.assertEqual(Calculator(2, -2, "-").calculate(), 4)

    def test_subtraction_with_zero(self):
        self.assertEqual(Calculator(0, 5, "-").calculate(), -5)

    def test_subtraction_both_negative(self):
        self.assertEqual(Calculator(-5, -3, "-").calculate(), -2)


    #Multiplication
    def test_multiplication_method_matches_calculate(self):
        calc = Calculator(7, 3, "*")
        self.assertEqual(calc.multiplication(), calc.calculate())

    def test_multiplication(self):
        self.assertEqual(Calculator(2, 2, "*").calculate(), 4)

    def test_multiplication_zero(self):
        self.assertEqual(Calculator(2, 0, "*").calculate(), 0)

    def test_multiplication_negative(self):
        self.assertEqual(Calculator(2, -2, "*").calculate(), -4)

    def test_multiplication_floats(self):
        self.assertAlmostEqual(Calculator(3.14, 2.0, "*").calculate(), 6.28, places=5)

    def test_multiplication_large_numbers(self):
        self.assertEqual(Calculator(10000, 10000, "*").calculate(), 100000000)

    def test_multiplication_both_negative(self):
        self.assertEqual(Calculator(-5, -3, "*").calculate(), 15)


    # Division
    def test_division_method_matches_calculate(self):
        calc = Calculator(7, 3, "/")
        self.assertEqual(calc.division(), calc.calculate())

    def test_division(self):
        self.assertEqual(Calculator(2, 2, "/").calculate(), 1)

    def test_division_by_zero(self):
        calc = Calculator(10, 0, "/")
        with self.assertRaises(ZeroDivisionError):
            calc.calculate()

    def test_division_floats(self):
        self.assertAlmostEqual(Calculator(7.5, 2.5, "/").calculate(), 3.0, places=5)

    def test_division_zero_numerator(self):
        self.assertEqual(Calculator(0, 5, "/").calculate(), 0)

    def test_division_negative(self):
        self.assertEqual(Calculator(-10, 2, "/").calculate(), -5)

    def test_division_both_negative(self):
        self.assertEqual(Calculator(-10, -2, "/").calculate(), 5)

    def test_division_result_float(self):
        self.assertAlmostEqual(Calculator(5, 2, "/").calculate(), 2.5, places=5)


    #Extra
    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            Calculator(5, 3, "%")

    def test_invalid_operation_symbol(self):
        with self.assertRaises(ValueError):
            Calculator(5, 3, "^")

    def test_very_small_numbers(self):
        self.assertAlmostEqual(Calculator(0.0001, 0.0002, "+").calculate(), 0.0003, places=10)


if __name__ == '__main__':
    unittest.main()
