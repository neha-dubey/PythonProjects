#Find the maximum total from top to bottom of the triangle below:
'''Get the maximum value for adjacent cells in current row.
        Update the cell which would be one step prior in the path
        with the new total. For example, compare the first two
        elements in row 15. Add the max of 04 and 62 to the first
        position of row 14.This provides the max total from row 14
        to 15 starting at the first position. Continue to work up
        the triangle until the maximum total emerges at the
        triangle's apex.'''

num=[[75],[95,64],[17,47,82],[18,35,87,10],[20,04,82,47,65],[19,01,23,75,03,34],[88,02,77,73,07,63,67],[99,65,04,28,06,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,04,68,89,53,67,30,73,16,69,87,40,31],[04,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]


sum=0
l=len(num)-1
for i in range(l, -1, -1):
    for j in range(0,i):
	num[i-1][j] += max(num[i][j], num[i][j+1])

print num[0][0]
