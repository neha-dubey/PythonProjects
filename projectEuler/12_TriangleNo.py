'''The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?'''


t=1
a=1
count=0
while count <= 500:
  count=0
  a += 1
  t = t+a

#If a number n has a divisor below n/2 then it has a corresponding divisor above n/2
  for i in range(1,int(t**0.5)):
    if t % i == 0: count += 2
  if int(t**0.5) == float(t**0.5): count -= 1

print t
