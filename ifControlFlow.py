number = 23
value = 'N'

while (value == 'N'):
 print "\n\n"
 input = int(raw_input('Guess the integer: '))

 if input == number:
	print "\n\nCongratulations you did it !!!"
        value = 'Y'

 elif input < number:
	print "\n\nSorry the number is a bit higher."
        print "Awwwwwwww BD !!! :("
	value = raw_input("Are you giving up BD(Y/N) ???")
      
 else: 
       print "\n\nSorry the number is a bit lower."
       print "Awwwwwwww BD !!! :("
       value = raw_input("Are you giving up BD(Y/N) ???")

print "Exiting now !!!"
