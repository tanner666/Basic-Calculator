"""A simple flask web app (This connects the pages)"""
from flask import Flask
from controllers.index_controller import IndexController
from controllers.calculator_controller import CalculatorController
from controllers.subpage_controller import SubpageController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# pylint: disable=missing-function-docstring
@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()


@app.route("/subpage1", methods=['GET'])
def oop_get():
    return SubpageController.get_oop()


@app.route("/subpage2", methods=['GET'])
def solid_get():
    return SubpageController.get_solid()


@app.route("/subpage3", methods=['GET'])
def tips_get():
    return SubpageController.get_tips_and_tricks()


@app.route("/subpage4", methods=['GET'])
def aaa_get():
    return SubpageController.get_aaa_testing()


@app.route("/results", methods=['GET'])
def results_get():
    return SubpageController.get_results()
