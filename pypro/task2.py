'''
Take list of integer numbers, print all number which are divisible by both 5 and 3.

'''

x = input('enter:')

print [i for i in x if i%5==0 and i%3==0]
