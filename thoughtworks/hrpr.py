
'''
sum of  numbers which are in the even positions

'''


N = int(raw_input())

x = map(int, raw_input().split())

total = 0
for i in xrange(1, N+1):
    if i%2==0:
        total += x[i]

print total
