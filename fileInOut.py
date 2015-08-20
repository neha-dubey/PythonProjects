var=2
poem = '''Hello how have you been
Waited for you
too long...


finally found you now.
''' + str(var) + '''
Done adding a variable value as well.'''

f = open("sample.txt", "a+")   #By default the file is opened in 't' mode (text)
			      # and not b (binary)
f.write(poem)
f.close()

f = open("sample.txt")
while True:
	line = f.readline()
	if len(line) == 0:
	 break
	print line

f.close()
