"""Division class"""


class Division:
    """This is the Division Class"""

    @staticmethod
    def divide(value_a, value_b):
        """Divide Function"""
        if value_b == 0:
            return "Divide By Zero Exception"
        return value_a / value_b

    @staticmethod
    def placeholder():
        """placeholder function to allow successful pylint test"""
        return
