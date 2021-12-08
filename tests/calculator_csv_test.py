"""Calculator Functions Test using csv files"""
import unittest

from calculator.calculator import Calculator
from csv_manager.file_reader import FileReader


class CalculatorTestCSV(unittest.TestCase):
    """Tests the Calculator functions using data from csv files"""

    # You have to add the fixture function as a parameter to the test that you want to use it with
    def test_calculator_add(self):
        """testing the addition method"""
        data = FileReader.csv_in('csv_manager/CSV_TestFiles/AdditionTest.csv')
        for data_set in data.itertuples():
            data = data_set[:-1]
            Calculator.addition(data)
            self.assertEqual(Calculator.get_result_value(), data_set[-1])

    def test_calculator_subtract(self):
        """Testing the subtract method"""
        data = FileReader.csv_in('csv_manager/CSV_TestFiles/SubtractionTest.csv')
        for data_set in data.itertuples():
            data = data_set[:-1]
            Calculator.subtraction(data)
            self.assertEqual(Calculator.get_result_value(), data_set[-1])

    def test_calculator_multiply(self):
        """Testing the multiply method"""
        data = FileReader.csv_in('csv_manager/CSV_TestFiles/MultiplicationTest.csv')
        for data_set in data.itertuples():
            data = data_set[:-1]
            Calculator.multiplication(data)
            self.assertEqual(Calculator.get_result_value(), data_set[-1])

    def test_calculator_divide(self):
        """Testing the divide method"""
        data = FileReader.csv_in('csv_manager/CSV_TestFiles/DivisionTest.csv')
        for data_set in data.itertuples():
            data = data_set[:-1]
            Calculator.division(data)
            if Calculator.get_result_value() == "ZeroDivisionError":
                self.assertEqual(Calculator.get_result_value(), data_set[-1])
            else:
                self.assertEqual(Calculator.get_result_value(), float(data_set[-1]))