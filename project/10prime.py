

import math
l = [2]
for num in xrange(3, 2000000, 2):
    if all(num%i != 0 for i in xrange(2, int(math.sqrt(num))+1)):
        l.append(num)
        print sum(l)
