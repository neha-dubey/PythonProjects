#Find the sum of the digits in the number 100.

import math
sum=0

fact=math.factorial(100)

#Convert factorial to a string
fact_str=str(fact)

for i in range(len(fact_str)-1):
  sum += int(fact_str[i])

print sum
