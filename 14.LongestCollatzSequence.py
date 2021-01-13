""" The following iterative sequence is defined for the set of positive integers:n → n/2 (n is even), n → 3n + 1 (n is odd). Using the rule above and starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1. Which starting number, under one million, produces the longest chain?"""

# Expected answer - 525

import time
start = time.time()

def sequence(number):
    length = 1
    while number != 1 :
        if number % 2 == 0:
            number = number//2
            length += 1
        else:
            number = 3 * number + 1
            length +=1
    return length

def maxLengthOfSequence(n):
    maxlength = 1
    for i in range(1,n+1):
        length = sequence(i)
        if length >= maxlength:
            maxlength = length
    return maxlength

print(maxLengthOfSequence(1000000))
end = time.time()

print('Duration:', round(end-start))

