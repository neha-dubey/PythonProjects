#What is the 10 001st prime number?

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


count_prime=1
number=3

#The while loop will continue until we reach to 10,001th prime
while count_prime < 10001:
  result = is_prime(number)
  if result:
 	count_prime += 1
  number += 2

print "10,001th prime number is ", number-2
