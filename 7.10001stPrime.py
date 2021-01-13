""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 
10001st prime number? """

# Expected answer - 104743

import math

list =[]
i=1
while len(list) < 10001:
    i += 1
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        list.append(i)
       
print(list[-1])
    