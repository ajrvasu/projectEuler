""" Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid? """

# Expected answer - 137846528820

# The math behind this is factorial and the Binomial coeeficient gives the results for any such grid

import math

def paths(n,k):
    paths = int((math.factorial(n+k))/ (math.factorial(n) * math.factorial(k)))
    return paths

print(paths(20,20))
