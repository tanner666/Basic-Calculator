""" This is the increment function (top layer of calculator)"""

from calculator.history.calc_history import History


class Calculator:
    """ This is the Calculator class"""

    # the calculator class calls methods from History class
    @staticmethod
    def get_result_value():
        """ This is gets the value of the calculation"""
        return History.get_last_calculation_value()

    @staticmethod
    # tuple allows for passing in multiple values
    def add_numbers(tuple_values: tuple):
        """ calls history addition method to add values"""
        History.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ calls history subtraction method to subtract values"""
        History.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ calls history multiplication method to multiply values"""
        History.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ calls history division method to divide values"""
        History.add_division_calculation(tuple_values)
        return True
