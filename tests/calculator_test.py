"""Calculator Functions Test"""
import unittest

from calculator.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    """Tests the Calculator functions"""

    # You have to add the fixture function as a parameter to the test that you want to use it with
    def test_calculator_add(self):
        """testing the addition method"""
        # pylint: disable=unused-argument,redefined-outer-name
        my_tuple = (1.0, 2.0, 5.0)
        Calculator.add_numbers(my_tuple)
        self.assertEqual(Calculator.get_result_value(), 8)

    def test_calculator_subtract(self):
        """Testing the subtract method"""
        # pylint: disable=unused-argument,redefined-outer-name
        my_tuple = (1.0, 2.0, 3.0)
        Calculator.subtract_numbers(my_tuple)
        self.assertEqual(Calculator.get_result_value(), -4)

    def test_calculator_multiply(self):
        """Testing the multiply method"""
        # pylint: disable=unused-argument,redefined-outer-name
        my_tuple = (1.0, 2.0, 3.0)
        Calculator.multiply_numbers(my_tuple)
        self.assertEqual(Calculator.get_result_value(), 6)

    def test_calculator_divide(self):
        """Testing the divide method"""
        # pylint: disable=unused-argument,redefined-outer-name
        my_tuple = (8.0, 4.0, 2.0)
        Calculator.divide_numbers(my_tuple)
        self.assertEqual(Calculator.get_result_value(), 1)

        # test for zero division error
        my_tuple = (8, 0, 1)
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide_numbers(my_tuple)
            Calculator.get_result_value()
