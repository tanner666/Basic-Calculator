"""Subtraction Class"""


from calculator.calculations.calculation import Calculation


class Subtraction(Calculation):
    """This is the subtraction Class"""

    def get_result(self):
        """get the subtraction results"""
        subtraction_of_values = self.values[0] * 2
        for value in self.values:
            subtraction_of_values = subtraction_of_values - value
        return subtraction_of_values
