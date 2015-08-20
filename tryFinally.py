import sys
import time

try:
 f = open("sample.txt")   #By default open() considers file in 't'ext and 'r'ead mode.
 while True:
  line = f.readline()
  if len(line) == 0:
   break
  print line
  sys.stdout.flush()
  time.sleep(2)
  print "Enter ctrl+C to check exception: "
 
except IOError:
 print "File could not be reached."

except KeyboardInterrupt:
 print "You interrupted while reading the file."

finally:
 if f:
	f.close()
 print "Closing the file now !!!"
