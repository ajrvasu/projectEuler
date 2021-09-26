""" Evaluate the sum of all the amicable numbers under 10000. """

import math,time

start = time.time()

def sumDivisors(n):
    sum = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            sum = sum + i + n//i
    return sum - n

def isamicable(a,b):
    if sumDivisors(a) == b and sumDivisors(b) == a:
        return True
    else:
        return False

def amicable_numbers(n):
    list = []
    total = 0
    for i in range(1,n):
        j = sumDivisors(i)
        if sumDivisors(j) == i and i != j:
            list.append(tuple(sorted((i,j))))    

    for tup in set(list):
        total += sum(tup)
    return total, set(list)

print(amicable_numbers(1000))

end = time.time()
print("Duration:", (end-start),"sec")
