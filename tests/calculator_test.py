"""Testing the Calculator"""

from calculator.calculator import Calculator


def test_calculator_add():
    """testing that our calculator has a static addition method"""
    result = Calculator.add_number(1, 2)
    assert result == 3


def test_calculator_subtract():
    """testing that our calculator has a static subtraction method"""
    result = Calculator.subtract_number(1, 2)
    assert result == -1


def test_calculator_multiply():
    """Testing the multiply method of the calculator"""
    result = Calculator.multiply_number(1, 2)
    assert result == 2


def test_calculator_divide():
    """Testing the divide method of the calculator"""
    result = Calculator.divide_number(6, 2)
    assert result == 3
    result = Calculator.divide_number(6, 0)
    assert result == "Divide By Zero Exception"
