

'''
Given a list of strings, return a list with the strings, in sorted order, except group all the strings that begin with 'x' first. Input ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'], output ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

'''


x = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

#x.sort()
l1 = []
l2 = []
for i in x:
    if i.startswith('x'):
        l1.append(i)
        l1.sort()
    else:
        l2.append(i)
        l2.sort()
        
print l1+l2

    
        
