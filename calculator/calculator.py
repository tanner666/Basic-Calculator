""" This is the increment function"""
# first import the addition namespace
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division


class Calculator:
    """ This is the Calculator class"""
    # this is the calculator static property
    history = []

    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        addition = Addition(args)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def clear_history():
        """ Clear the calculation history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculator.history[num]

    @staticmethod
    def get_calculation_last():
        """ get last calculation from history"""
        return Calculator.history[-1]

    @staticmethod
    def subtract_numbers(*args):
        """ subtract numbers"""
        subtraction = Subtraction(args)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """ multiply numbers"""
        multiplication = Multiplication(args)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(*args):
        """ divide numbers and store the result"""
        division = Division(args)
        Calculator.history.append(division)
        return division.get_result()
