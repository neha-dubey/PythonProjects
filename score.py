score=float(raw_input("Enter a score in the range 0.0 - 1.0: "))
if score > 1.0:
    print "Score not in range. Exiting now !!!"
    quit()
elif score < 0.0:
    print "Score not in range. Exiting now !!!"
    quit()
    
if score >= 0.9:
    print "A"
    
elif score >= 0.8:
    print "B"
    
elif score >= 0.7:
    print "C"
    
elif score >= 0.6:
    print "D"
    
elif score < 0.6:
    print "F"
