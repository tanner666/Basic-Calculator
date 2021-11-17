"""Division class"""

from calculator.calculations.calculation_factory \
    import Calculation


class Division(Calculation):
    """This is the Division Class"""

    def get_result(self):
        """get the division results"""
        total = self.values[0] ** 2
        for value in self.values:
            try:
                total /= value
            except ZeroDivisionError as error:
                raise ZeroDivisionError from error
        return total
