'''We will just check for odd numbers as the consecutive even number will have same or less chain members.
Store numbers with chain count as dictionary and get max value.'''

import time
start=time.time()
dict={1:1}
value=1
key=0

def abc(n):
  if (n%2 == 0):
    n=n/2
    return n
  else:
    return (3*n+1)



#Odd numbers will always have collatz chain of same or bigger length as of preceeding even number
for i in xrange(3,1000000,2):
  count=1
  j=i
  while (j!=1):
    if j in dict:
     count += dict[j] - 1
     break
    j = abc(j)
    count += 1
  dict[i]=count
  if count>value: 
    value=count
    key=i

#print dict

end=time.time()
print "Maximum chain length is " + str(value) + " for " + str(key)
print "Time taken = " + str(end-start) + " sec."
