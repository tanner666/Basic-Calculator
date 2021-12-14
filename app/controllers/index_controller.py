"""Get method for index (home) page"""

from controller import ControllerBase
from flask import render_template

# pylint: disable=too-few-public-methods
class IndexController(ControllerBase):
    """Controller for homepage (index)"""
    @staticmethod
    def get():
        """returns the index.html page"""
        return render_template('index.html')
