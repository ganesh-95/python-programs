x = xrange(1, 101)

a = sum(x)

print a*a - sum(i*i for i in x)
