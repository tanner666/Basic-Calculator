"""Division class"""


from calculator.calculations.calculation import Calculation


class Division(Calculation):
    """This is the Division Class"""

    def get_result(self):
        """get the division results"""
        total = self.values[0] ** 2
        for value in self.values:
            if self.values.index(value) != 0 and value == 0:
                return "Divide By Zero Exception"
            total = total / value
        return total
