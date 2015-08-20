""" The idea is to isolate the largest powers of primes within a range, in our case, 20 and then divide out the additional primes, leaving out only the largest of primes in the list. This idea works because others are composite numbers and composite numbers are simply the product of primes. We find the combination of primes that can give out all the numbers within the list of 1 to 20. This is done by first multiplying all numbers from 2 to 20 and then isolating the primes as required"""

# This function gets the max power of a prime within a number

def max_power(p):
   k = 0
   n = 20
   for x in range(int(n**0.5)+1):
	if p**x < n:
	  k = x
   return k


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


# This gives the product of numbers from 2 to 20
#num = reduce(lambda x, y: x * y, range(2,21), 1)

number = 1

# This part of the code isolates the primes as required
for i in range(2,21):
    if is_prime(i):
      po = max_power(i)
      #while num % i == 0:
#	num = num/i
#      num = num*(i**po)
      number *= (i**po) #This calculation uses the logic to multiply all prime numbers with the maximum power 
                                #such that if p[i] is a prime then p[i] ^x <= N (N is 20 in our case)


print "The smallest multiple is: ", number
