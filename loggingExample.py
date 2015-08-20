#This code is created to test logging module in Python by creating logger.
#Study two classes located in logging.handlers module (inside logging package).
#The classes are:
#  1. RotatingFileHandler
#  2. WatchedFilehandler

import logging
from logging import handlers

#Custom log file creation
LOG_FILENAME='/home/neha/python/customLog.log'

#Create logger
lgr = logging.getLogger('myApp')
lgr.setLevel(logging.INFO)

#Add a file handler
fh=logging.FileHandler(LOG_FILENAME)
fh.setLevel(logging.INFO)

#Set log rotation to handler
fh=logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1000, backupCount=10)

#Create a formatter
frmt=logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

#Set formatter for the handler
fh.setFormatter(frmt)

#Add handler for the logger
lgr.addHandler(fh)

#Issuing logging statements in the code
lgr.debug('Debugging statement here')
lgr.error('You encountered an error')
lgr.warning('Warning being displayed')
lgr.info('Info logging')
lgr.critical('You have encountered a critical error...Be careful !!!')





#Sample code to test logging functionality
#This code calculates the occurance of a specific
#line in a text file

fname = raw_input("Enter the file name: ")
file = open(fname)
addition = 0
count = 0
for line in file:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        xline = float(line[19:])
        addition += xline
        count += 1


average = addition/count
print "Average spam confidence:", average

