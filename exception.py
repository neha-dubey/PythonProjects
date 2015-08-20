class specialCharactersException(Exception):

	'''User defined exception class derived from Exception class'''

	def __init__(self, character):
	 Exception.__init__(self)
	 self.character = character

try:
	input = raw_input("Enter the string without special characters: ")
	SkippedChar = '''!@#$%^&*;:"?.~`'''
	for char in SkippedChar:
	 if char in input:
		raise specialCharactersException(char)

except EOFError:
	print "Encountered End Of File at the input."

except specialCharactersException as ex:
	print "Encountered a special character " + ex.character + " which is not allowed."	

else:
	print "No exception encountered."
