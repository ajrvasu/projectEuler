""" The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143"""

# Expected answer - 6857

import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
            break
    return True

def largestPrimeFactor(n):
    factor = 0
    for i in range(1,int(math.sqrt(n))):
        if n % i == 0 and isPrime(i):
            factor = i
    return factor

print(largestPrimeFactor(600851475143))