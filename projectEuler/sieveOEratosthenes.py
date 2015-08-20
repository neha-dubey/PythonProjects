# The Sieve of Eratosthenes method works here as well, with last few lines modified to suit the problem

num = int(raw_input("Enter the number you wish to find all primes under: "))
start_list = list(range(num + 1))
#
for ind1 in range(2, int(num ** 0.5) + 1):
    if start_list[ind1] != 0:
        for ind2 in range(ind1 * 2, num + 1, start_list[ind1]):
            start_list[ind2] = 0
#
# Isolating the primes
primes = []
for index in range(2, num + 1):
    if start_list[index] != 0:
        primes.append(start_list[index])

print sum(primes)
