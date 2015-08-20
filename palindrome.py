
#This uses slicing of string to reverse it
def reverse(text):
	#print "Reverse string is: "+ (text[::-1])
	return text[::-1]        



# Verifies if the string is a palindrome
def is_palindrome(text):
	return punct == reverse(text)

input = raw_input("Enter a string: ")


# To remove all puntuations from the string
forbidden = """',. -":;*&$%@!?"""
punct = ""

for char in input:
	if char not in forbidden:
	  punct = punct + char
	

if is_palindrome(punct):
	print "\nString is a palindrome.\n"
else:
	print "\nString is not a palindrome.\n"
