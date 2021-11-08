"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator
from calculator.history.history import History


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    History.clear_history()


# You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0, 2.0, 5.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_result_value() == 8.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0, 2.0, 3.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_result_value() == -4.0


def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0, 2.0, 3.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_result_value() == 6.0


def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    # using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (8.0, 4.0, 2.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_result_value() == 1.0
    my_tuple = (8.0, 0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_result_value() == "Divide By Zero Exception"
