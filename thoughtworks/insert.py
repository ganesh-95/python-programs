#inserting a number into sorted array

import bisect

a = [12, 34, 34, 23, 22, 9, 8, 100]

b = sorted(a)

bisect.insort(b,93)

print b
