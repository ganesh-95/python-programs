"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""def is_polindrome(num):
    return str(num) == str(num)[::-1]

def largest(bot,top):
    z = 0
    for x in range(top, bot, -1):
        for y in range(top, bot, -1):
            if is_polindrome(x*y):
                if x*y > z:
                    z = x*y


    return z
print largest(100, 999)
