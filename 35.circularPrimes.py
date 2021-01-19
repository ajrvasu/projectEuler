"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime. There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How many circular primes are there below one million?"""

# Expected answer - 55

import math
import itertools 

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
            break
    else:
        return True

def permutations(n):
    lst = list(itertools.permutations(str(n)))
    permutations =[]
    primes =[]
    unique =[]
    for tuple in lst:
        permutations.append(''.join(tuple))
    for number in permutations:
        if not isPrime(int(number)):
            break
    else:    
        primes.append(int(number))
    unique = list(set(primes))
    return unique

def circularPrimes(n):
    circularPrimes =[]
    for i in range(2,n+1):
        circularPrimes.append(permutations(i))
    flat = [item for sublist in circularPrimes for item in sublist]
    return sorted(list(set(flat))), len(sorted(list(set(flat))))

print(circularPrimes(100000))