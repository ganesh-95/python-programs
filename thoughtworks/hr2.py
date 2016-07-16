'''
factorial with recursion

here set_recursion_limit is used
because in python recursion limit is upto 999 

'''
import sys
sys.setrecursionlimit(1050)
x = input()

def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
        

print factorial(x)
