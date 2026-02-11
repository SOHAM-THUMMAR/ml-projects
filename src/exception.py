import sys
import logging


def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return f"Error in {file_name}, line {line_number}: {error}"


class CustomException(Exception):
    def __init__(self, error):
        super().__init__(str(error))
        self.error_message = error_message_detail(error)

    def __str__(self):
        return self.error_message
