'''
if a number when reversed, the square of the number and the square of the reversed number should be numbers which are reverse of each other. this is ADAM number
'''


N = input()

strlst = str(N**2)

strrev = ''.join(list(reversed(strlst)))

if strrev == str(N**2)[::-1]:
    print 'adam number'
else:
    print 'not adam number'
