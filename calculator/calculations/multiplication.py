"""Multiplication class"""

from calculator.calculations.calculation_factory \
    import Calculation


class Multiplication(Calculation):
    """This is the Multiplication Class"""

    def get_result(self):
        """gets the multiplication results"""
        total = 1.0
        for value in self.values:
            total = value * total
        return total
