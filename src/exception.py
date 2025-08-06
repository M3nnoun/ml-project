import sys
import logging
import logger
def error_message_detailed(error ,error_detail:sys):
    _,_, exc_tb = sys.exc_info()
    error_message ='Error occurred in script: [{0}] at line number: [{1}] with message: [{2}]'.format(
        exc_tb.tb_frame.f_code.co_filename,
        exc_tb.tb_lineno,
        str(error))
    return error_message

class CustomException(Exception):
    def __init__(self , error_message , error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detailed(error_message, error_detail)
    
    def __str__(self):
        return self.error_message
    

