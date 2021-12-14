"""Testing csv_manager Functions"""
import os.path
import time
import pandas
from csv_manager.file_writer import FileWriter
from csv_manager.file_reader import FileReader
import main


def test_calculate():
    """Tests the calculate method in main"""
    # Arrange
    file = 'csv_manager/CSV_TestFiles/CalculateTest.csv'
    data = FileReader.csv_in(file)
    array_final = []
    # Act
    main.calculate('division', file, data)
    logs = FileReader.csv_in('csv_manager/Results/calculator_log.csv')
    for log in logs.itertuples():
        array_final.append(log)
    # Assert
    assert array_final[-1][4] == '5.0'


def test_csv_in():
    """testing FileReader"""
    # Arrange
    filename = 'MoveTest.csv'
    path = 'csv_manager/CSV_TestFiles'
    full_path = path + '/' + filename
    # Act
    data_frame = FileReader.csv_in(full_path)
    # Assert
    assert isinstance(data_frame, pandas.DataFrame)


def test_move_to_completed():
    """testing move file to completed folder function"""
    # Arrange
    filename = 'MoveTest.csv'
    path = 'csv_manager/CSV_TestFiles'
    full_path = path + '/' + filename
    final_path = 'csv_manager/CSV_CompletedFiles' + '/' + filename
    # Act
    FileWriter.move_to_completed(full_path)
    # Assert
    assert os.path.exists(final_path)


def test_log():
    """testing log function (writes results in log file)"""
    # Arrange
    filename = 'LogTest.csv'
    array = [str(time.time()), filename, '1', 'addition', '1']
    array_final = []
    # Act
    FileWriter.log([array], 'calculator_log.csv')
    logs = FileReader.csv_in('csv_manager/Results/calculator_log.csv')
    for log in logs.itertuples():
        array_final.append(log)
    # Assert
    assert array_final[-1][0] == array[0]


def test_exceptions_log():
    """testing exceptions log function (writes exceptions in corresponding file)"""
    # Arrange
    filename = 'DivisionTest.csv'
    array_final = []
    # Act
    FileWriter.log_exceptions(filename, 'T')
    logs = FileReader.csv_in('csv_manager/Results/exceptions_log.csv')
    for log in logs.itertuples():
        array_final.append(log)
    # Assert
    assert array_final[-1][2] == 'T'


def test_log_line_counter():
    """testing a function that returns the number of lines in a csv file"""
    file = 'csv_manager/CSV_TestFiles/AdditionTest.csv'
    lines = FileReader.line_counter(file)
    assert lines == 8
