
'''
armstrong number
'''


N = int(raw_input())

X = N
sum = 0

while N>0:
    d = N%10
    sum += d**3
    N //= 10
if sum == X:
    print 'armstrong'
else:
    print 'not armstrong'

