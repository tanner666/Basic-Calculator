"""Get method for subpages"""
from flask import render_template
from controller import ControllerBase
from csv_manager.file_reader import FileReader


# pylint: disable=missing-function-docstring
class SubpageController(ControllerBase):
    """controller class for all subpages"""
    @staticmethod
    def get_oop():
        return render_template('OOP_in_calc.html')

    @staticmethod
    def get_solid():
        return render_template('SOLID_in_calc.html')

    @staticmethod
    def get_tips_and_tricks():
        return render_template('tips_and_tricks.html')

    @staticmethod
    def get_aaa_testing():
        return render_template('AAA_testing.html')

    @staticmethod
    def get_results():
        data = FileReader.csv_in('csv_manager/Results/website_results_log.csv')
        data_array = []
        for data_set in data.itertuples():
            data_array.append(data_set)

        return render_template('result_log.html', data=data_array)
