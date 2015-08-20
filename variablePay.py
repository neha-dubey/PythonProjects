condition='N'

while (condition=='N'):
	inputHours=raw_input("\n\nEnter number of work hours: ")

	try:
	  hours=float(inputHours)
	except:
	  print "Please enter a numeric input for hours."

	inputRate=raw_input("Enter rate per hour: ")

	try:
          rate=float(inputRate)
        except:
          print "Please enter a numeric input for rate."


	if (hours > 40):
		pay = (rate * 40) + (hours-40)*rate*1.5
		print "Pay is: " + str(pay) + "\n(Since hours are greater than 40)"
		condition=raw_input("Do you want to exit(Y/N): ")
	else:
		pay = rate * hours
		print "Pay is: " + str(pay) + "\n(Hours being less than or equal to 40)"
		condition=raw_input("Do you want to exit(Y/N): ")

print "Exiting now !!!\n\n"
