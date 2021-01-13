""" Tt can be verified that T285 = P165 = H143 = 40755. Find the next triangle number that is also pentagonal and hexagonal """

# Expected answer - 1533776805

import time
start = time.time()

def tph():
    k = 1
    while True:
        p = k*(3*k-1)//2 
        hlist = [i*(2*i-1) for i in range(1,k+1)]
        if p in hlist:
            yield p
        k += 1

number = tph()
series = []

for i in range(1,4):
    series.append(next(number))

print(series)

end = time.time()
print(f"Duration is {round(end-start)} sec")
        

