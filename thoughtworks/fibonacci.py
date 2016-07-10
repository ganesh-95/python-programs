#fibonacci series.. nth number in series

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

x = input('enter the nth number:')

print fib(x)
