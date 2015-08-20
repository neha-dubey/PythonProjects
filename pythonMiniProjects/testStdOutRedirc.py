#This is to test redirecting stdout and strerr to log files

import sys

print "Before redirecting standard output"
saveout = sys.stdout
with open('testLog.txt', 'w') as f:
  sys.stdout = f
  print "After redirecting standard output"
  sys.stdout = saveout
  print "After redirection ends"

print "Log file closed now !! :)"
