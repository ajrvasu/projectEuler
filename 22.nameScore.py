""" Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score. For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714. What is the total of all the name scores in the file? """

# Expected answer - 871198282

f = open('euler22.txt')
string = f.readlines()
f.close()

names = sorted(string[0].split(","))
nameList = [i.replace('"','') for i in names]

from string import ascii_uppercase
from collections import OrderedDict

alphabet = OrderedDict((k, i+1) for i, k in enumerate(ascii_uppercase))

def nameScore(names):
    nameScore = 0
    for i in range(len(names)):
        score = 0
        for letter in names[i]:
            value = alphabet[letter]
            score += value
        nameScore += score * (i+1)
    return nameScore

print(nameScore(nameList))

