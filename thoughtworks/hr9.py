
'''
second largest number among the  numbers
'''


y = int(raw_input())

N = raw_input()

x = list(N.split())
x.sort(key=int)
print x[1]
