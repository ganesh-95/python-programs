
1.
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


 2.

 a = input()

def find(arr):
    for x in range(1,len(arr)-1):
        if x not in arr:
            return x

print find(a)

        
