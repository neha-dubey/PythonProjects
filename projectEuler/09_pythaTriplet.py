'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

max=1000

for a in range(max):
  for b in range(a+1,max):
    for c in range(b+1,max):
	if a+b+c == max:
	  if (a*a)+(b*b) == (c*c):
	    print "Product for required pythagorean triplet is: ", a*b*c
	    quit()
