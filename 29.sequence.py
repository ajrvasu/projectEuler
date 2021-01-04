"""How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100? """


def distinctTerms(n):
    list =[]
    [list.append(i**j) for i in range(2,n+1) for j in range(2,n+1)]
    sequence =[]
    [sequence.append(k) for k in list if k not in sequence]
    return len(sequence)

print(distinctTerms(100))