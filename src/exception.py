import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message




'''
def error_message_detail(error, error_detail: sys):
error → the actual exception message (like division by zero).
error_detail: sys → the system module used to get information about the error.

exc_info() returns three things:
exception type
exception object
traceback (where the error happened)
You only need the traceback, so _ ignores the first two values.

file_name = exc_tb.tb_frame.f_code.co_filename
This finds the Python file where the error occurred.
Example:
train.py

error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
)
This builds a formatted string containing:
file name
line number
actual error

'''