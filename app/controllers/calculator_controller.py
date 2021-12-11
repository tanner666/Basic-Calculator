"""Defines what the post and get method do"""
from csv_manager.file_writer import FileWriter
from csv_manager.file_reader import FileReader
from app.controllers.controller import ControllerBase
from calculator.calculator import Calculator
from calculator.history.calc_history import History
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    """Post and get method"""
    @staticmethod
    def post():
        value1 = request.form['value1']
        value2 = request.form['value2']

        valid_values = True
        try:
            float(value1) and float(value2)
        except ValueError:
            valid_values = False

        if value1 == '' or value2 == '':
            error = 'You must enter a value for value 1 and or value 2!'
        elif not valid_values:
            error = 'You must enter valid values!'
        else:
            flash('Calculation successful!')
            # flash('You are awesome')

            # get the values out of the form
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_result_value())

            FileWriter.log([[FileReader.log_line_counter('csv_manager/Results/website_results_log.csv')+1,
                             operation, value1, value2, result]], 'website_results_log.csv')
            data = FileReader.csv_in('csv_manager/Results/website_results_log.csv')
            data_array = []
            for data_set in data.itertuples():
                data_array.append(data_set)

            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result,
                                   data=data_array)

        return render_template('calculator2.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator2.html')
