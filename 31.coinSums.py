""" In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins? """

# i*0.01+j*0.02+k*0.05+l*0.1+m*0.2+n*0.5+o*1+p*2

def coinSums():
    count = 0
    for i in range (0,200):
        for j in range(0,100):
            for k in range(0,40):
                for l in range(0,20):
                    for m in range(0,10):
                        for n in range(0,4):
                            for o in range(0,2):
                                for p in range(0,1):
                                    if i*0.01+j*0.02+k*0.05+l*0.1+m*0.2+n*0.5+o*1+p*2 == 2:
                                        count += 1
    return count

print(coinSums())

