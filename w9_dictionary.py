'''Problem: Write a program to read through the sample2.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

APPROACH:
1. Open the file
2. Read it by line in a loop
3. If line starts from 'From' store it in a list
4. Loop through list and read second word and store it to dict - increment count
5. When loop for step-2 is over run another loop to find max occurance'''

input=raw_input("Enter the file to be read: ")
if len(input) < 1:
  input='sample2.txt'

lst=[]
counts={}
with open(input) as fh:
  while True:
    line=fh.readline()
    if not line: break
    if line.startswith("From "):
	lst=line.split()
	counts[lst[1]]=counts.get(lst[1],0)+1
	#for word in lst:
	#  counts[word]=counts.get(word,0)+1

    
c=None
data=None
for key,value in counts.items():
  if data == None or value>data:
    c = key
    data = value

print "Maximum emails have been received from " + key + " and emails received are " + str(data)



##Alternate way for with open():

#fh=open(input)
#for line in fh:
#  if line.startswith("From "):
#    <Rest of the code goes here>
