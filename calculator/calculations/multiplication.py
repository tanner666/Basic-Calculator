"""Multiplication class"""


from calculator.calculations.calculation import Calculation


class Multiplication(Calculation):
    """This is the Multiplication Class"""

    def get_result(self):
        """get the multiplication results"""
        total = 1.0
        for value in self.values:
            total = value * total
        return total
