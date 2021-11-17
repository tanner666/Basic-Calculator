"""Calculation History Class"""
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division


class History:
    """History class stores and handles calculations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clears the history of all calculations"""
        History.history.clear()
        return True

    @staticmethod
    def count_history():
        """gets the number calculations stored in history"""
        return len(History.history)

    @staticmethod
    def get_last_calculation_value():
        """gets the value of the last calculation"""
        return History.history[-1].get_result()

    @staticmethod
    def get_calculation(num):
        """ gets a specific calculation from history"""
        return History.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ adds a calculation to history"""
        return History.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """Adds an addition object to history"""
        History.add_calculation(Addition.create(values))
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """Adds a subtraction object to history"""
        History.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Adds a multiplication object to history"""
        History.add_calculation(Multiplication.create(values))
        return History.get_last_calculation_value()

    @staticmethod
    def add_division_calculation(values):
        """Adds a division object to history"""
        History.add_calculation(Division.create(values))
        return True
