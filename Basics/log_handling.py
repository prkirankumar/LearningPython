'''
- captures and records events while app is running .
- useful debugging feature
  not always practical to debug in real time
- Events can be categorized for easier analysis
- provides transaction record of a program's execution

severity levels

DEBUG-  logging.debug() - Diagnostic information useful for debugging
INFO- logging.info() - General information abotu program execution results
WARNING- logging.warning() - something unexpected, or an approaching problem
ERROR- logging.error() - unable to perform a specific operation due to problem 
CRITICAL- loggin.critical() - program may not be able to continue, serious error


customized logging
%(asctime)s - Huma readable date format when the log record was created
%(filename)s - filename where the log message originated
%(funcname)s - function name where the log message originated
%(levelname)s - string representation o the message level (DEBUG,INFO, etc)
%(levelno)d - numeric representation of the message level
%(lineno)d - source line number where the logging cals was issued (if available)
%(message)s - the logged message string itself
%(module)s - module name portion of the filename where the message was logged

'''
# to use logging module
import logging


extData={'user' : 'user@domain.com'}

#logging.basicConfig(filename='demolog.log',level=logging.DEBUG)
# We pass a filename argument to the logging.basicConfig() method. Here, we call our file demolog.log. Such a file is one we can consult over time.

# displaying datetime in log
#logging.basicConfig(filename='demolog.log',format='%(asctime)s %(message)s', level=logging.DEBUG) # filemode='w'  creates new file every time , if not provided it will be appended
formatstring="User : %(user)s %(asctime)s : %(levelname)s : %(lineno)d %(message)s"
datestr="%m/%d/%Y %I:%M:%S %p" # %p is for am or pm
logging.basicConfig(filename='demolog.log',format=formatstring, level=logging.DEBUG,datefmt=datestr)

logging.warning("You are warned with timestamp",extra=extData)
logging.warning('%s before %s','Service','self',extra=extData)
# Setting logging format