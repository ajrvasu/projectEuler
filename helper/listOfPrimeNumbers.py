import math

def listOfPrimes():
    n = int(input("Enter a number :"))
    if n > 1:
        list =[]
        for i in range(2,n+1):
            for j in range(2,int(math.sqrt(i))+1):
                if i % j == 0:
                    break
            else:
                list.append(i)
        print(list)
        print(len(list))
    else:
        print("Not a valid input, enter a whole number which is greater than 1.")

listOfPrimes()
