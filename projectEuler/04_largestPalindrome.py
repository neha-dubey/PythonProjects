#Find the largest palindrome made from the product of two 3-digit numbers.
numb1 = 999
maxprod = 0
while numb1 > 100:
 numb2 = 999
 while numb2 > 100:
	prod = numb1 * numb2
	stprod = str(prod)
	palin = stprod[::-1]
	if palin == stprod:
	  if prod > maxprod: 
	  #print "Largest palindrome is: ",prod
	  #print "numbers are: " + str(numb1) + " " + str(numb2)
	      maxprod = prod
	numb2 = numb2 - 1
 numb1 = numb1 - 1

print "Largest palindrome is: ",maxprod



#def Palindrome(n):
#    i = str(n)
#    k = len(i)
#    return all(i[e] == i[k-1-e] for e in range(0,k))
#dud = []
#for i in (900000,1000000):
#    if palindrome(i) == True:
#        dud.append(i)
#    print max(dud)  
