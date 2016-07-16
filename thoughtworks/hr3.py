'''
prime number between range
'''




x = input()
for num in xrange(1,x+1):
    if all(num%i!=0 for i in xrange(2,num)):
       print num
