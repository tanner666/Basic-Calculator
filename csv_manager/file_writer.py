"""File writer class"""
import shutil
import time
import pandas as pd
from csv_manager.file_reader import FileReader


class FileWriter:
    """File Writer"""

    @staticmethod
    def log(array, file):
        """Prints results to the log file"""
        # noinspection PyTypeChecker
        # pylint: disable=line-too-long
        pd.DataFrame(array).to_csv(FileReader.absolute_path('csv_manager/Results/' + file),
                                   mode='a', index=False, header=False)

    @staticmethod
    def move_to_completed(file):
        """moves file to completed folder"""
        shutil.move(file, FileReader.absolute_path('csv_manager/CSV_CompletedFiles'))

    @staticmethod
    def log_exceptions(filename, record_num):
        """Prints results to the exceptions file"""
        data_frame = pd.DataFrame([[time.time(), filename, record_num, 'division',
                                    'Zero Division Error']])
        # noinspection PyTypeChecker
        data_frame.to_csv(FileReader.absolute_path('csv_manager/Results/exceptions_log.csv'),
                          mode='a', index=False, header=False)
