'''
1st programme : four elements sum 

'''

from  itertools import permutations

final_elements = []

a = input()


x = input()

desired_total = input()


for i in permutations(a, x):	
    if any(True for j in final_elements if j in i):
        continue
    if sum(i) == int(desired_total):
        print i
        final_elements.extend(i)

print final_elements
