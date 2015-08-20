maximum = None
minimum = None

while True:
 input = raw_input("Enter a number: ")
 if input == "done":
	break

 try:
  numb = int(input)
  if minimum is None:
    minimum = numb
  elif numb < minimum:
    minimum = numb

  if maximum is None:
    maximum = numb
  elif numb > maximum:
    maximum = numb


 except:
  print "Invalid input"


print "Maximum is",maximum
print "Minimum is",minimum



