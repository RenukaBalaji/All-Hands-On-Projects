import os
import sys

class AppException(Exception):
    """
    Custom exception class for the Book Recommender System application.
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = AppException.get_detailed_error_message(error_message, error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error: Exception, error_detail: sys):
        """
        Constructs a detailed error message including the file name and line number where the exception occurred.
        """
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = f"Error occurred in file: {file_name} at line number: {line_number} with error message: {str(error)}"
        return error_message
        
    def __repr__(self):
        return AppException.__name__.__str__()


    def __str__(self):
        return self.error_message