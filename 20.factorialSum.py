""" Find the sum of the digits in the number 100! """

# Expected answer - 648

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)    

print(sum(int(i) for i in str(factorial(100))))
