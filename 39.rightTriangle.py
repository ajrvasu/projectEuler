"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50}. For which value of p ≤ 1000, is the number of solutions maximised? """

import time

start = time.time()

def triplets(n):
    triplets =[]
    for a in range(1,n):
        for b in range(a,n):
            c = n-a-b
            if a**2 + b**2 == c**2:
                triplets.append((a,b,c))
    return len(triplets)

def perimeter(n):
    maxtriplets = 0
    index = 0
    solutions ={}
    for i in range(1,n+1):
        solutions[i] = triplets(i)
    
    for key in solutions:
        if solutions[key] > maxtriplets:
            maxtriplets = solutions[key] 
            index = key

    return index, maxtriplets

print(perimeter(1000))

end = time.time()
print('Duration:', round(end-start), 'sec')