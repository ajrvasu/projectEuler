""" 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What 
is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """

# Expected answer - 232792560

import math

def isdivisible(n,k):
    for i in range (1,k+1):
        if n % i != 0:
            return False
    return True

def smallestNumber(n):
    fact = math.factorial(n)
    smallestNumber = 1
    while smallestNumber <= fact:
        if isdivisible(smallestNumber,n) is False:
            smallestNumber +=1
        else:
            return smallestNumber

print(smallestNumber(20))