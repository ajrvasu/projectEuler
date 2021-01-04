""" Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 
9474 
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316. Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

# The maximum uppper bound is 5 * 9^5 =295_245, round off to 300_000

import time
start = time.time()

def fifthPowerNumbers():
    list =[]
    for i in range(2,300_000):
        digits = [int(j) for j in str(i)]
        if sum(j**5 for j in digits) == i:
            list.append(i)
    return sum(number for number in list)

print(fifthPowerNumbers())

end = time.time()
print("Duration:", round(end-start),"sec")


