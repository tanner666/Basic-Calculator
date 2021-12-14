"""Defines what the post and get method do"""
from controller import ControllerBase
from flask import render_template, request, flash
from csv_manager.file_writer import FileWriter
from csv_manager.file_reader import FileReader
from calculator.calculator import Calculator
from calculator.history.calc_history import History


class CalculatorController(ControllerBase):
    """Post and get method"""
    # pylint: disable=missing-function-docstring
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

            # this method returns an array containing the [operation name, tuple of values, result]
            # I did this just to connect the csv log to the History Class
            h_data = History.get_info(-1)
            # pylint: disable=line-too-long
            FileWriter.log([[FileReader.line_counter('csv_manager/Results/website_results_log.csv')+1,
                            h_data[0], h_data[1][0], h_data[1][1], h_data[2]]], 'website_results_log.csv')

            # stores rows of data from csv log in a data_array (which is passed into result.html)
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
