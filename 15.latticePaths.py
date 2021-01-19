""" Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid? """

# Expected answer - 137846528820

def latticePaths(i,j, memoize = {}):
    key = str(i) + ',' + str(j)
    if i == 0 or j == 0: return 1
    if i == 1 and j == 1: return 2
    if key in memoize:
        return memoize[key]
    memoize[key] =  latticePaths(i-1,j) + latticePaths(i,j-1)
    return memoize[key]

print(latticePaths(20,20))
