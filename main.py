"""Main driver class of Calculator"""
from os import listdir
import time
import os
from csv_manager.file_reader import FileReader
from csv_manager.file_writer import FileWriter
from calculator.calculator import Calculator


def calculate(operation, file_name, data):
    """performs calculations on a file and logs the results"""
    array = []
    record_num = 1
    for data_set in data.itertuples():
        getattr(Calculator, operation)(data_set)
        if Calculator.get_result_value() == "ZeroDivisionError":
            FileWriter.log_exceptions(file_name, record_num)
        array.append([time.time(), file_name, record_num, operation,
                      Calculator.get_result_value()])
        record_num += 1
    FileWriter.log(array, file_name)


def main():
    """driver function (searches input files folder, computes operations,
    moves files to completed folder)"""
    input_folder_path = FileReader.absolute_path('csv_manager/CSV_InputFiles')
    if not os.listdir(input_folder_path):
        print("empty")
    else:
        print("full")
        files = listdir(input_folder_path)
        for file in files:
            file = 'csv_manager/CSV_InputFiles/' + file
            data = FileReader.csv_in(FileReader.absolute_path(file))
            calculate('addition', file, data)


if __name__ == '__main__':
    main()
