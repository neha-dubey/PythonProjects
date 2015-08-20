#!/usr/bin/python2.7

# This is a logs cleanup script that will cleanup logs based on following:
#	1. Check logs older than a specified date/time
#	2. For older logs create a folder named 'archive'
#	3. Make a tar of all such older logs and store it in archive dir as:
#		* A separate folder with date stamp
#		* tar file inside this folder with name having size of the file



import os
import time
from datetime import datetime
import re
import shutil
import tarfile
import sys



def archive_logs(f):
  shutil.copy((os.path.join(logs_path, f)),temp_arch_path)  
  

def create_tar():
  dateTime = datetime.now().strftime("%Y%m%d")
  fileName = "arch_" + dateTime + ".tar.gz"
  tar_file_path = os.path.join(arch_path, fileName)
  with tarfile.open(fileName, "w:gz") as tar:
    tar.add(temp_arch_path, arcname=os.path.basename(temp_arch_path))
  print "\n\nMoving tar file to archive directory..."
  if os.path.exists(tar_file_path):
    new_name = os.path.join(arch_path, fileName + "_2")
    os.rename(tar_file_path, new_name)
    print "Tar file already there, renaming it"
  shutil.move(os.path.join(path, fileName), arch_path)
    


def create_archive_dir(arch_path):
  if not os.path.exists(arch_path):
    os.makedirs(arch_path)
    print "Creating the required archive directory"
  print "Archive directory already exists."
  if not os.path.exists(temp_arch_path):
    os.makedirs(temp_arch_path)
    print "Creating a temporary archive"


##Defining global variables
path = '/home/neha/python/pythonMiniProjects/'
logs_path = os.path.join(path, 'logs')
temp_arch_path = os.path.join(path, 'temp_archive')
arch_path = os.path.join(path, 'archive')

def main():
  ##Redirecting standard output to a txt file
  saveout = sys.stdout
  fhandler = open('logsCleanup.txt', 'w')
  sys.stdout = fhandler

  create_archive_dir(arch_path)

  ##This section identifies logs to be archived and copies them to a temp location
  files = os.listdir(logs_path)
  for f in files:
   if os.path.isfile(os.path.join(logs_path, f)):
     regexp = re.compile(r'.+_logs.txt') #in place of this we could directly use
			 	       # re.search(pattern, string)
     if regexp.search(f) is not None: 
       timeStampOfFile = os.stat(os.path.join(logs_path, f)).st_mtime
       currentTime = time.time()
       arcLogTime = currentTime-(1*86400/2)  #This will delete logs older than a week
       if timeStampOfFile < arcLogTime:
         archive_logs(f)


  ##This section will create tar of archive logs and delete temp directory
  print "Creating a tar file now..."
  create_tar()
  print "Deleting temporary archive directory..."
  shutil.rmtree(temp_arch_path)


  ##Deleting old logs finally
  for f in os.listdir(logs_path):
    if f.endswith(".txt"):
    #if os.path.isfile(os.path.join(logs_path, f)):
      if os.stat(os.path.join(logs_path, f)).st_mtime < (time.time()) - 1*86400/4:
        os.remove(os.path.join(logs_path, f))
        print "Cleaned old logs."
  
  fhandler.close()
  sys.stdout = saveout


if __name__ == '__main__':
  main()
