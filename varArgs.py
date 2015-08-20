def func(initial, *numbers, **arguments):
	count=initial
	print count
	for x in numbers:
		count += x
	for y in arguments:
		count += arguments[y]
	return count

print func(10,1,2,3,v=50,t=100)
