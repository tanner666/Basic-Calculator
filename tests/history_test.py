"""Testing the Calculator"""
import pytest
from calculator.history.calc_history import History
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division


@pytest.fixture
def clear_history_fixture():
    """runs before each test to clear the history list"""
    # pylint: disable=redefined-outer-name
    History.clear_history()


@pytest.fixture
def setup_addition_calculation_fixture():
    """runs before each test to add two values to the history list"""
    # pylint: disable=redefined-outer-name
    values = (2, 1)
    History.add_addition_calculation(values)
    History.add_subtraction_calculation(values)
    History.add_multiplication_calculation(values)
    History.add_division_calculation(values)


def test_clear_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 4
    History.clear_history()
    assert History.count_history() == 0
    assert History.clear_history() == True


def test_count_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing the count method of history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.count_history() == 4


def test_get_last_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation object from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # This test if it returns the last calculation as an object
    assert isinstance(History.get_last_calculation(), Division)


def test_get_last_calculation_value(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation value from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_last_calculation_value() == 2


def test_get_first_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the first calculation object from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert isinstance(History.get_first_calculation(), Addition)


def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_calculation(0).get_result() == 3


def test_add_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing that a calculation is successfully appended to history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    History.add_calculation(History.add_division_calculation((3, 1)))
    assert History.get_calculation(4).get_result() == 3


def test_add_addition_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing that an addition object is successfully inserted into history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.get_calculation(0).get_result() == 3


def test_add_subtraction_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing that a subtraction object is successfully inserted into history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.get_calculation(1).get_result() == 1


def test_add_multiplication_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing that a multiplication object is successfully inserted into history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.get_calculation(2).get_result() == 2


def test_add_division_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing that a division object is successfully inserted into history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.get_calculation(3).get_result() == 2
