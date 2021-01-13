""" If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
3 + 3 + 5 + 4 + 4 = 19 letters used in total.If all the numbers from 1 to 1000 (one thousand) inclusive 
were written out in words, how many letters would be used?"""

# Expected answer - 

def count(n):
    string = ''
    letters_1 = ['one','two','three','four','five','six','seven','eight','nine']
    letters_2 = ['ten','twenty','thrity','forty','fifty','sixty','seventy','eighty','ninety']
    letters_3 = ['','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    letters_4 = ['onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred']
    if n < 10:
        numbers = [i for i in range(1,n+1)]
        for i in range(len(numbers)):
            index = i
            string += letters_1[index]
        return string, len(string)

print(count(5))
