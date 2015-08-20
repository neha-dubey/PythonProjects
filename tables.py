input = int(raw_input("Enter the number for multiplication table to be displayed: "))

for i in range(1,11):
	print str(input) + " * " + str(i) + " = " + str(input*i)
