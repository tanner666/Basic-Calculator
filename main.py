"""Main driver class of Calculator"""
from os import listdir
import shutil
import time
import os
import pandas as pd
from file_reader import FileReader
from calculator.calculator import Calculator


def log(array, file):
    """Prints results to the log file"""
    # noinspection PyTypeChecker
    pd.DataFrame(array).to_csv(FileReader.absolute_path('CSV_Files/Results/calculator_log.csv'),
                               mode='a', index=False, header=False)
    shutil.move(file, FileReader.absolute_path('CSV_Files/CSV_CompletedFiles'))


def log_exceptions(file, record_num):
    """Prints results to the exceptions file"""
    data_frame = pd.DataFrame([[time.time(), file, record_num, 'division',
                                'Zero Division Error']])
    # noinspection PyTypeChecker
    data_frame.to_csv(FileReader.absolute_path('CSV_Files/Results/exceptions_log.csv'),
                      mode='a', index=False, header=False)


def add(file, data, array):
    """adds"""
    record_num = 1
    for data_set in data.itertuples():
        Calculator.addition(data_set)
        array.append([time.time(), file, record_num, 'addition',
                      Calculator.get_result_value()])
        record_num += 1
    log(array, file)


def subtract(file, data, array):
    """subtracts"""
    record_num = 1
    for data_set in data.itertuples():
        Calculator.subtraction(data_set)
        array.append([time.time(), file, record_num, 'subtraction',
                      Calculator.get_result_value()])
        record_num += 1
    log(array, file)


def multiply(file, data, array):
    """multiplies"""
    record_num = 1
    for data_set in data.itertuples():
        Calculator.multiplication(data_set)
        array.append(
            [time.time(), file, record_num, 'multiplication',
             Calculator.get_result_value()])
        record_num += 1
    log(array, file)


def divide(file, data, array):
    """divides"""
    record_num = 1
    for data_set in data.itertuples():
        Calculator.division(data_set)
        if Calculator.get_result_value() == "ZeroDivisionError":
            log_exceptions(file, record_num)
            array.append([time.time(), file, record_num, 'division', Calculator.get_result_value()])
        record_num += 1
    log(array, file)


def main():
    """driver function"""
    input_folder_path = FileReader.absolute_path('CSV_Files/CSV_InputFiles')
    if not os.listdir(input_folder_path):
        print("empty")
    else:
        print("full")
        files = listdir(input_folder_path)
        for file in files:
            array = []
            file = 'CSV_Files/CSV_InputFiles/' + file
            data = FileReader.csv_in(FileReader.absolute_path(file))
            add(file, data, array)


if __name__ == '__main__':
    main()
