""" Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""

# Expected answer - 5537376230

# Converting number.txt file into a list of digits 

filename = "euler13.txt"

with open(filename,"r") as lines:
    array =[]
    for line in lines:
        array.append(line)

newArray =[]
for i in array:
    j = i.split(' ')
    k = [int(n) for n in j]
    newArray.append(k)

list = sum(newArray, [])


def largeSum(n,list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return (str(sum))[:n]

print(largeSum(10,list))
