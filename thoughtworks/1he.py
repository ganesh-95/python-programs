'''
for given array, print the set of numbers which are equal to the given total
'''


arr = [1, 2, 3, 4, 5, 6]

l = []

def sum_1(arr, total):
    if not arr:
        return
    if arr[i] == total:
        l += i
        del arr[i]
    else:
        sum_1(arr, total)
        return l
        
        
        
    
print sum_1(arr, 9)
        

