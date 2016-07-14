'''
Take a list of words(ex: ['python', 'php', 'c', 'java', 'perl']) print words which are starts and ends with p. Note: Try to use for loop.
'''

x =  ['python', 'php', 'c', 'java', 'perl']

l = []

for i in x:
    if i.startswith('p') and i.endswith('p'):
        l.append(i)

print l
