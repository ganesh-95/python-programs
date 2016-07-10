
from  itertools import permutations

final_elements = []

a = input()
output_list_length = input("enter list count ")
desired_total = input("enter list total ")
for i in permutations(a, int(output_list_length)):
    if any(True for j in final_elements if j in i):
        continue
    if sum(i) == int(desired_total):
        print i
        final_elements.extend(i)
print final_elements
