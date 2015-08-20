#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f=open('13_Sum50Num.txt').read().split()
addition=sum(map(int,f))
print str(addition)[:10]
