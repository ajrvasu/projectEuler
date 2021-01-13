""" How many, not necessarily distinct, values of (n r) for 1 <= n <= 100, are greater than one-million?  """

# Expected answer - 4075

# Triangular number is always a Hexagonal number. So equality has to be checked only between Pentagonal and Hexagonal numbers. 

import time
from math import factorial as fac

start = time.time()

def selections(k):
    count = 0
    for n in range(1,k+1):
        for r in range(0,n):
            if fac(n) // (fac(n-r)*fac(r)) > 1_000_000:
                count +=1 
    return count

print(selections(100))

end = time.time()
print(f"Duration is {round(end-start)} sec")
