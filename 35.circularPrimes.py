"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime. There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How many circular primes are there below one million?"""

import math
from itertools import permutations

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
            break
    else:
        return True
    
def permutation(n):
    list =[int(i) for i in str(n)]
    newLst = []
    for i in permutations(list):
        newLst.append(i)
    numbers = [int(''.join([str(j) for j in i]))for i in newLst]
    return numbers

def circularPrimes(n):
    circularPrimes =[]
    for i in range(2,n+1):
        for j in range(len(permutation(i))):
            if isPrime(permutation(i)[j]) == True:
                circularPrimes.append(permutation(i)[j])
    return circularPrimes

def length(n):
    list = circularPrimes(n)
    sortedList = sorted(list)
    uniqueList =[]
    [uniqueList.append(i) for i in sortedList if i !=1 and i not in uniqueList]
    return uniqueList
            
print(circularPrimes(100))
print(length(100))