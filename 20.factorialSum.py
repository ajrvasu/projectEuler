""" Find the sum of the digits in the number 100! """

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)    
number = factorial(100)
print(number)

def factorialSum(number):   
    sum = 0
    for i in str(number):
        sum += int(i)
    print(sum)

factorialSum(number)

"""
print(sum(int(i) for i in str(factorial(100))))
"""
        

