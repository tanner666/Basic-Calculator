"""Addition Class"""
from calculator.calculations.calculation_factory \
    import Calculation


class Addition(Calculation):
    """This is the Addition Class"""

    def get_result(self):
        """gets the addition result"""
        total = 0.0
        for value in self.values:
            total = value + total
        return total
