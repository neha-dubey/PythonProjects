#Find the sum of all the multiples of 3 or 5 below 1000.


##Alternate and easy way of solving this query:
#x = xrange(1,1000)
#sum = 0
#for numb in x:
#	if numb % 3 == 0:
#	    sum = sum + numb
#	    continue
#
#	if numb % 5 == 0:
#	    sum = sum + numb
#
#print "Sum of all mutiples of 3 or 5 below 1000 is: ", sum


##Another way to solve using generator function():
def multiple():
  for i in xrange(1000):
	if not i % 3 or not i % 5:
	   yield i

print "Sum of all mutiples of 3 or 5 below 1000 is", sum(multiple())
