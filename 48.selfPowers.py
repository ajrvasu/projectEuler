""" The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317. Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000 """

# Expected answer - 9110846700

def selfPowers(n):
    number = str(sum(i**i for i in range(1,n+1)))
    return number[-10:]

print(selfPowers(1000))