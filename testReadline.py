#This is just to check readline function working with blank lines

file = raw_input("Enter file to be read: ")
count = 0
'''with open(file) as f:
  while True:
    line = f.readline()
    count += 1
    if not line: break

print "There are ", count, "lines in the file"'''

f = open(file)
for line in f:
 count += 1

print "There are ", count, "lines in the file"
