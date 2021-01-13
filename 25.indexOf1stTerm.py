"""What is the index of the first term in the Fibonacci sequence to contain 1000 digits? """

# Expected answer - 17

def fibIndex(n):
    prev, curr = 1,1
    list = [prev,curr]
    while curr < n:
        prev,curr = curr, prev + curr
        list.append(curr)
    print("Index of the first term in the sequence to contain",n,"digits is", len(list),".")

fibIndex(1000)

    