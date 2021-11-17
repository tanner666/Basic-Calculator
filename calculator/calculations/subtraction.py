"""Subtraction Class"""


from calculator.calculations.calculation_factory \
    import Calculation


class Subtraction(Calculation):
    """This is the subtraction class"""

    def get_result(self):
        """gets the subtraction results"""
        total = self.values[0] * 2
        for value in self.values:
            total = total - value
        return total
