import logging

#in format, we can format, how we want to update the log file.
# as per below format variable, first, the time will be displayed, i.e. %(asctime)s
# then the log level, i.e. %(levelname)s
# and then the message, i.e %(message)s
# E.G. : "2020-04-29 21:11:37,796 : WARNING : This is a warning message."
# we also can change the format of the time in 'datefmt' variable.
# datefmt = ''
logging.basicConfig(filename="log.log",  #this is the file path
                    #format = '%(asctime)s : %(name)s : %(levelname)s : %(message)s',
                    format = '%(asctime)s : %(levelname)s : %(message)s',
                    datefmt= '%d/%m/%Y %I:%M:%S %p',
                    level= logging.DEBUG, #this means, initial level is Debug, to add log in log file
                )

logging.debug("This is basic log message.") #This will not be displayed on console
logging.info("This is info log message.") #This will not be displayed on console
logging.warning("This is a warning message.") #This will be displayed on console with red font color
logging.error("This is an error message.") #This will be displayed on console with red font color
logging.critical("This is a critical error message.") #This will be displayed on console with red font color