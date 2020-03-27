# Problem 15 - Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#  __ __
# |__|__|  <- Grid
# |__|__|
# How many such routes are there through a 20×20 grid?
#
# Answer: 137846528820

# This problem can be solved with brute force method but its not recommended for big numbers.
# In 2x2 grid there are 4 moves before i reach bottom right corner.
# So i have to choose 2 of the 4 moves to be down and the rest are right.
# Combination type ( discrete maths ) : n! / [r! * (n-r)! ] , where n are all the move options and r the down move options.
# At 2x2 grid , n=4 and r=2 so 4!/[2! * 2!] = 6
# So in 20x20 grid , n=40 and r=20

import math

def problem15():
    n = 40
    r = 20
    possible_paths = math.factorial(n) / ( math.factorial(r) * math.factorial(n-r) )
    print(int(possible_paths))


problem15()