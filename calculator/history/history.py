"""Calculation history Class"""
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division


class History:
    """Calculations class manages the history of calculations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        History.history.clear()
        return True

    @staticmethod
    def count_history():
        """get number of items in history"""
        return len(History.history)

    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return History.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = History.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return History.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return History.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        return History.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        History.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        History.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        History.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Add a division object to history using factory method create"""
        History.add_calculation(Division.create(values))
        return True
