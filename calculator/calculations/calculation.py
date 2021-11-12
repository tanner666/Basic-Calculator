"""General Calculation class"""


class Calculation:
    """ abstract base class for the 4 calculations"""

    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    @classmethod
    def create(cls, values: tuple):
        """ factory method where all objects get instantiated (centralized)"""
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_of_float(values):
        """ converts args to a tuple of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
