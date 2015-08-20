def computepay(h, r):
    if h > 40:
        pay = (r*40) + (h-40)*1.5*r
        return pay
    else:
        pay = r*h
        return pay
    
try:    
	hours=int(raw_input("Enter the number of hours: "))
	rate=float(raw_input("Enter rate per hour: "))
except:
	print "Please enter numeric input"
	quit()

print "Total pay is: " + str(computepay(hours, rate))
