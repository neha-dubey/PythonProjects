'''Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.'''

file=raw_input("Enter file name to be opened: ")
if len(file) < 1: file='sample.txt'
lst=list()
with open(file) as f:
  for line in f:
    wrds=line.split()
    i=0
    while i < len(wrds):
	if wrds[i] not in lst:
	  lst.append(wrds[i])
	i += 1	
	

lst.sort()  #sort method replaces the existing list so no need to assign it 
	    #to a new variable, else it will return 'none' as output
print lst


#Another method but error prone as we have to manually close the file
'''file=raw_input("Enter file name: ")
lst=list()
f = open(file)
for line in f:
    wrds = line.split()
    for word in wrds:
        if word not in lst:
            lst.append(word)
          
f.close()
lst.sort()
print lst'''

