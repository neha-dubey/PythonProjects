#==============================================================================
# Using Combinatorics we can make the calculation using factorials
# Since the path can move either down or right, for a 2x2 grid, we have the following paths
# 1. RRDD 2.DDRR 3.RDRD 4.DRDR 5.DRRD 6.RDDR
# Each path consists of 2 rights and 2 downs. Hence for a NxN grid, there would be N downs and N rights.
# The paths of length 2N with all the combinations of R and D. If we have all D, then the places of R's are automatically determined
# In terms of combinatorics, what are the different ways to choose N out of 2N if the order does not matter?
# 2N choose N !
#==============================================================================

import math as m
def sqgrid(n):
    return ((m.factorial(2*n))/((m.factorial(n))**2))

print sqgrid(20)
