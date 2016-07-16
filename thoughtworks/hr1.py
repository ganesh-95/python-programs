'''
factorial of a number

'''
x = input()

def factorial(x):
    if x == 0:
        return 1
    else:
        result = 1
        for i in xrange(2, x + 1):
            result *= i
    return result

print factorial(x)


