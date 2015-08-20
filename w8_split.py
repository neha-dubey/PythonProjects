'''Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.'''

fname=raw_input("Enter file name to be read: ")
if len(fname) < 1: fname='sample2.txt'  #If user does not input file name 
					#then default file name is assigned

count = 0
with open(fname) as f:      #Opening with 'with' closes the file after 'with' 
			    #indentation block is over
  while True:
    line = f.readline()     #Reads one line at a time in memory
    if not line: break
    line.strip()
    if line.startswith("From "):
  	  count += 1
	  string = line.split()
	  print string[1]
    #if len(line) == 0: break

print "\nThere were " + str(count) + " lines in the file with From as the first word"
