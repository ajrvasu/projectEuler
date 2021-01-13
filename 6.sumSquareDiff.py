""" The sum of the squares of the first ten natural numbers is 385 (1^2+2^2+....+10^2). The square of the sum of the 
first ten natural numbers is 3025 ((1+2+....10)^2). Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 2640.Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum. """

# Expected answer - 25164150

print((sum([i for i in range(1,101)]))**2 - sum([i**2 for i in range(1,101)]))