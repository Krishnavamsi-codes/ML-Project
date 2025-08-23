import sys
import logging
## sys library has functions and variables that are used to manipulate different parts of the runtime environment
def error_message_detail(error,error_detail:sys):
 #     type → The exception class (e.g., ZeroDivisionError, ValueError, etc.)

 # value → The exception instance (the actual error object with the message).

 # traceback → A traceback object that points to the call stack at the moment the exception was raised.
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


        


