""" In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins? """

# Expected answer - 67379

import time
start = time.time()

def coinSums():
    count = 0
    for i in range (0,3):
        for j in range(0,5):
            for k in range(0,11):
                for l in range(0,21):
                    for m in range(0,41):
                        for n in range(0,101):
                            for o in range(0,201):
                                if i*1+j*0.5+k*0.2+l*0.1+m*0.05+n*0.02+o*0.01 == 2:
                                    count += 1
    return count + 1

print(coinSums())

end = time.time()
print(f"Duration is : {round(end-start)} sec")
