import sys

def errorMessageDetail(error, errorDetail:sys):
  _,_,exc_tb = errorDetail.exc_info()

  fileName = exc_tb.tb_frame.f_code.co_filename
  lineNumber = exc_tb.tb_lineno
  error = str(error)

  errorMessage = f"There is error is {fileName} line number {lineNumber} error message {error}"

  return errorMessage


class CustomException(Exception):
  def __init__ (self, errorMessage, errorDetail:sys):
    super.__init__(errorMessage)
    self.errorMessage = errorMessageDetail(errorMessage, errorDetail=errorDetail)

  def __str__(self):
    return self.errorMessage
  
