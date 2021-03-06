#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2=552=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

sum_of_sq = 0
sq_of_sum = 0
temp_sum = 0
for i in range(1,101):
  sum_of_sq += i*i
  temp_sum += i

sq_of_sum = temp_sum**2
print "Difference is: ", (sq_of_sum - sum_of_sq)
