""" 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. What is the sum of the digits of the 
number 2^1000? """

sum = 0
for digit in str(2**1000):
    sum += int(digit)
print(sum)

# Using a generator expression

print(sum(int(i) for i in str(2**1000)))

# Using a list comprehension

print(sum([int(i) for i in str(2**1000)]))
