""" The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
We can see that 28 is the first triangle number to have over five divisors. What is the value of the first triangle number to have over five hundred divisors? """

def triangularNumber(number):
    sum = 0
    for i in range(1,number+1):
        sum += i
    return sum

def numberOfDivisors(d):
    divisors = []
    for i in range(1,d//2 + 1):
        if d % i == 0:
            divisors.append(i)
    divisors.append(d)
    return len(divisors)

def smallestTraingularNumber(n):
    number = 1
    while True:
        divisors = numberOfDivisors(triangularNumber(number))
        if divisors < n:
            number += 1
        else:
            return triangularNumber(number)    

print(triangularNumber(7))
print(numberOfDivisors(triangularNumber(7)))
print(smallestTraingularNumber(167))