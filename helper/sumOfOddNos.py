import math

def sumOfOddNos():
    n = int(input("Enter the number of odd nos: "))
    list =[]
    for i in range(1,2*n,2):
        list.append(i)
    print("The first",len(list), "odd numbers are",list, "and their sum is",n**2)

sumOfOddNos()
