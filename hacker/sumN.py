"""
sum of integers in a given array 
"""



array = map(int, raw_input().split())

print(sum(int(n) for n in array))
