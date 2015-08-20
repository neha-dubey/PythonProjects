#!/usr/bin/python

'''This program will generate logs daily at a specified directory with the
log file names having date and time and just a sample text.

Steps for developement would be:
1. Check if a directory already exists else create it
2. Create the log with specified name having date and time
3. Configure cronjob to execute py script at desired intervals
'''

import os
from datetime import datetime
import sys


def check_dir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)
    print "Create the required directory"
  print "Directory already existed"


def create_log(filePath, fileName):
  log_message = '''Log created at ''' + datetime.now().strftime('%Y-%m-%d---%H-%M-%S') + '''

This is a periodically generated log file to test the following:
1. logs generation.
2. Crontabs with Python
3. Logs cleanup.'''
  fullFileName = os.path.join(filePath, fileName)
  if not os.path.isfile(fullFileName):
    with open(fullFileName, 'a+') as f:
      f.write(log_message)
  else:
    fullFileName = fullFileName + "_2"
    with open(fullFileName, 'a+') as f:
      f.write(log_message)


def main():
  directory = '/home/neha/python/pythonMiniProjects/logs'
  check_dir(directory)
  dateTime = datetime.now().strftime("%Y%m%d_%H%M")
  fileName = dateTime + "_logs.txt"
  create_log(directory, fileName)

if __name__ == '__main__':
  main()
