#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

#Create a dictionary to store sum of letters for some numbers spelled so that it covers all possible combinations till 1000.
letterCount={0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7, 1000:11}

#range to check if a number falls in teen category of numbers(like 419,615,...)
chklst=range(11,20)

#To handle 'and' in spellings
a=3

sum=0

for i in range(21):
 sum += letterCount[i]

for i in range(21,100):
 sum += letterCount[(i/10)*10] + letterCount[i%10]

#Add count for 100
sum += letterCount[100] + letterCount[1]

for i in range(101,111):
  sum += letterCount[i/100] + letterCount[100] + a + letterCount[i%100]




#Separate treatment for numbers in teens(like: 119)

for i in range(111,1000):
  if(i%100 in chklst):
      sum += letterCount[i/100] + letterCount[100] + a + letterCount[i%100]
  elif(i%100 == 0):                         #These will not contain 'and'
      sum += letterCount[i/100] + letterCount[100]
  else:
      sum += letterCount[(i/100)] + letterCount[100] + a + letterCount[((i%100)/10)*10] + letterCount[(i%100)%10]

#Add count for 1000
sum += letterCount[1000]

print "Number letter count from 1-1000 is: " + str(sum) 
