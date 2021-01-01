
"""
import math

for i in range(2,int(math.sqrt(10))+1):
    print(i)

list = [1,2,3,4]
print(len(list)) 



sum = sum(i for i in range(1,11))
print(sum)


list = [i for i in range(1,11)]
print(list)
"""

print([i**j for i in range(2,5) for j in range(2,5)])