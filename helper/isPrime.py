import math

def isPrime():
    n = int(input("Enter a number:"))
    if n > 1:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                print("Is composite")
                break
        else:
            print("Is prime")
    else:
        print("Not a valid input")

isPrime()