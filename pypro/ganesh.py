import re

b = "WILLIAM ALLEY AMERICAN BRANDS died"
c = "AMB"
d = "1996"
e = "66"

f = open('output_B3.txt','r').read()

if 'WILLIAM' in f:
    if 'died' in f:
        if '1996' in f:
            if 'AMB' in f:
                if '349631' in f:
                    if '66' in f:
                        print 1
else:
    print 0
                    
