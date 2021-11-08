""" This is the increment function"""
# first import the addition

from calculator.history.history import History


class Calculator:
    """ This is the Calculator class"""

    # the calculator class just calls methods on History class
    @staticmethod
    def get_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return History.get_last_calculation_result_value()

    @staticmethod
    # tuple allows me to pass in as many values as a I want
    def add_numbers(tuple_values: tuple):
        """ adds list of numbers"""
        History.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        History.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiplication number from result"""
        History.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ divide numbers and store the result"""
        History.add_division_calculation(tuple_values)
        return True
