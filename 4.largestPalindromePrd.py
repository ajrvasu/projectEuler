"""A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers. """

def isPalindrome(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def largestPalindrome(n):
    max = 0
    for i in range(n):
        for j in range(n):
            if len(str(i*j)) % 2 == 0 and isPalindrome(str(i*j)):
                if i*j >= max:
                    max = i*j
    return max

print(largestPalindrome(1000))

