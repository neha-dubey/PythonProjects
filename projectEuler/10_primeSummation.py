#Find the sum of all the primes below two million.

# This function determines whether a number is prime or not

def is_prime(n):
   if n <= 3:
        return n >= 2
   if n % 2 == 0 or n % 3 == 0:
        return False
   for i in range(5, int(n**0.5)+1,6):
        if n % i == 0 or n % (i + 2) == 0:
          return False
   return True


sum=0
i=1
while i <= 2000000:
  result = is_prime(i)
  if result:
	sum += i
  i += 1

print "Summation of all primes below two million is: ", sum
