""" The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143"""

import math

def largestPrimeFactor(n):
    curr = 1
    for i in range(int(math.sqrt(n)),int(n/2)):
        if n % i == 0:
            curr = i
    if curr > 1:
        print(curr)
    else:
        print(n)

largestPrimeFactor(97)