#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?


#Store the 1000 digit number and convert it into a string
number=73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724271218839987979087922749219016997208880937766572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397

con_numb = str(number)
max_prod=1

#Loop-in the string for each set of 13 digits
for i in range(len(con_numb)-12):
    prod=1
    for j in range(13):
 	  con_int=int(con_numb[i+j])
	  prod *= con_int
	  if prod > max_prod:
	      max_prod = prod
	      pos = i           #Stores the initial position for the result set
print "The largest product is: ", max_prod
print "Digits included in the largest product are: "

for i in range(pos, pos+13):
  print con_numb[i]
