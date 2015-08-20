def is_leap_year(year):
  if (year % 400):
	return True
  elif (year % 100):
	return False
  elif (year % 4):
	return True
  else:
	return False

input = int(raw_input("Enter year to check for leap year: "))
result = is_leap_year(input)

if (result == True):
 print "The year " + str(input) + " is a leap year !!!"
else:
  print "The year " + str(input) + " is not a leap year."
