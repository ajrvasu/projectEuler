""" There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc. """

s = 1000
for a in range (1,s):
    for b in range(a,s):
        c = s-a-b
        if a**2 + b**2 == c**2:
            print(a,b,c) 
            
       
