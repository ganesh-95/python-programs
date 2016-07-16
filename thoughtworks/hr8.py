'''
given unsorted array, find minimum number which is not present in the array
'''


N  = int(raw_input())

x = map(int, raw_input().split())


y =  list(x)

y.sort(key=int)

print y[0]-1

