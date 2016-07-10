"""
Given an array of integers, find all combination of four elements in the array whose sum is equal to a given value X.
For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and X = 23, then your function should print ¡°3 5 7 8¡å (3 + 5 + 7 + 8 = 23).
"""


from  itertools import permutations

final_elements = []

a = input()
output_list_length = input("enter list count ")
desired_total = input("enter list total ")
for i in permutations(a, int(l_count):
    if any(True for j in final_elements if j in i):
        continue
    if sum(i) == int(total):
        print i
        final_elements.extend(i)


        
