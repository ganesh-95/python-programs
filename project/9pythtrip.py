'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''



import math

def pyth_trip():
    for a in xrange(500):
        for b in xrange(a+1, 500):
            c = 1000 - (a+b)
            if a**2 + b**2 == c**2:
                print a, b, c
                return a*b*c
print pyth_trip()
        


