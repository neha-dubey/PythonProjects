#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 

fname = raw_input("Enter the file name: ")
file = open(fname)
for line in file:
  line = line.rstrip().upper()
  print line
