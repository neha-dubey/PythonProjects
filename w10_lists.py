#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, as hour count in each line

file=raw_input("Enter file to open: ")
if len(file) < 1: file="sample2.txt"
count=dict()

with open(file) as f:
  while True:
    line=f.readline()
    if line.startswith("From "):
      words=line.split()
      req_word=words[5]
      time=req_word.split(":")
      hour=time[0]
      count[hour]=count.get(hour,0) + 1  #Creates or/and increments 
                                           #key,values in dictionaries
    if not line: break

res=count.items()
res.sort()

for k,v in res:
  print k,v
