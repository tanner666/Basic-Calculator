"""Division class"""

from calculator.calculations.calculation_factory \
    import Calculation


class Division(Calculation):
    """This is the Division Class"""

    def get_result(self):
        """get the division results"""
        total = self.values[0]
        for value in self.values[1:]:
            try:
                total /= value
            except ZeroDivisionError:
                return "ZeroDivisionError"
        return total
