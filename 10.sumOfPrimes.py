""" Problem 10 - Find the sum of all the primes below two million """

# Expected answer - 142913828922


import time
import math

start = time.time()

def sumOfPrimes(n):
    list =[]
    for i in range(2,n+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            list.append(i)
    return sum(i for i in list)
    
print(sumOfPrimes(2_000_000))

end = time.time()
print("Duration:", round(end-start),"sec")




