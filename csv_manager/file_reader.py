"""This reads in files"""
from pathlib import Path
import pandas as pd


class FileReader:
    """File Reader"""

    @staticmethod
    def csv_in(file):
        """Imports a csv file into a dataframe"""
        return pd.read_csv(file, header=None, index_col=0)

    @staticmethod
    def absolute_path(filepath):
        """Returns the absolute path of a file"""
        relative = Path(filepath)
        return relative.absolute()
