'''
 find all numbers between 1 and 1000 which are divisible by 3 but are not a multiple of 5.
'''

print [i for i in xrange(1, 1000) if i%3==0 and i%5!=0]
