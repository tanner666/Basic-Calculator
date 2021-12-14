"""Get method for index (home) page"""
# pylint: disable=no-name-in-module import-error
from flask import render_template
from app.controllers.controller import ControllerBase


# pylint: disable=too-few-public-methods
class IndexController(ControllerBase):
    """Controller for homepage (index)"""
    @staticmethod
    def get():
        """returns the index.html page"""
        return render_template('index.html')
