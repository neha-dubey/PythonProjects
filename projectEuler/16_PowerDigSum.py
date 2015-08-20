#What is the sum of the digits of the number 2 to the power 1000?

num=str(2**1000)

sum=0
i=0
while(i<len(num)):
  sum += int(num[i])
  i += 1

print sum

'''import math
def sod(n,debug = False):
    if debug == True:
        return n
    q = str(int(n))
    l = 0
    for i in range(len(q)):
        y = float(q[i])
        if debug == True:
            print "The current value in q is",y
        l += y
    return l
a = int(raw_input("Enter the number: "))
b = int(raw_input("Enter the power: "))
n = math.pow(a,b)
print sod(n)'''
