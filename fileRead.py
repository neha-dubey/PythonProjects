'''Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown'''

import os, platform, logging   #To import system(OS), platform(info about 
			       #platform) and logging related modules


if platform.platform().startswith('Windows'):
  logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'),
					'testLogFile.log')
else:
  logging_file = os.path.join(os.getenv('HOME'), 'testLogFile.log')

print "Logging to ", logging_file

#setting logging configurations:
logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s : %(levelname)s : %(message)s',
	filename = logging_file,
	filemode = 'w')

logging.debug("Start of the code")
logging.info("Doing something")
logging.warning("Bye")
logging.error("Encontered some errors")

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
