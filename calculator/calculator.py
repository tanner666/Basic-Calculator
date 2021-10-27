""" This is the calculator"""

from calculator.operations.addition import Addition
from calculator.operations.division import Division
from calculator.operations.multiplication import Multiplication
from calculator.operations.subtraction import Subtraction


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(value_a, value_b):
        """ adds two numbers"""
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract two numbers"""
        return Subtraction.subtract(value_a, value_b)

    @staticmethod
    def multiply_number(value_a, value_b):
        """ multiplies two numbers"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_number(value_a, value_b):
        """divides value_a by value_b"""
        return Division.divide(value_a, value_b)
