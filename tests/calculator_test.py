"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculator.clear_history()


# You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(1.0) == 1.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers(1.0, 2.0) == -1.0


def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiplication method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1.0, 2.0) == 2.0


def test_calculator_divide_static(clear_history_fixture):
    """ tests division method"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(2.0, 1.0) == 2
    assert Calculator.divide_numbers(9.0, 3.0) == 3
    assert Calculator.divide_numbers(1.0, 0.0) == "Divide By Zero Exception"


def test_calculator_history_static_property(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    Calculator.add_numbers(1.0, 2.0)
    assert len(Calculator.history) == 1


def test_clear_history():
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    Calculator.add_numbers(1.0, 2.0)
    assert Calculator.clear_history() == True


def test_get_calculation(clear_history_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    Calculator.add_numbers(1.0, 2.0)
    assert Calculator.get_calculation(0).get_result() == 3


def test_get_calculation_last(clear_history_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    Calculator.add_numbers(1.0, 2.0)
    assert Calculator.get_calculation_last().get_result() == 3
