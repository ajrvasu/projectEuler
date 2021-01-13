""" The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word. Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words? """

# Expected answer - 162

import math

def isTriangular(n):
    if (-1 + math.sqrt(1 + 8 * n)) % 2 == 0:
        return True
    return False

f = open('euler42.txt')
string = f.readlines()
f.close()

names = sorted(string[0].split(","))
nameList = [i.replace('"','') for i in names]

from string import ascii_uppercase
from collections import OrderedDict

alphabet = OrderedDict((k, i+1) for i, k in enumerate(ascii_uppercase))

def triangularNumbers(words):
    count = 0
    for word in words:
        value = 0
        for letter in word:
            value += alphabet[letter]
        if isTriangular(value):
            count += 1
    return count

print(triangularNumbers(nameList))