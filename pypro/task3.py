'''
 Take a list of words(ex: ['python', 'php', 'c', 'java', 'perl']) print words which are starts with p. Note: Try to use for loop.
'''

x =  ['python', 'php', 'c', 'java', 'perl']

l= []

for i in x:
    if i.startswith('p'):
        l.append(i)
print l
