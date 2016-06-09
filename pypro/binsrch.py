l = [1, 2, 3, 4, 8, 9, 34, 67, 89]
def bin_srch(l, x):
    min = 0
    max = len(l)-1
    while True:
        if max < min:
            return -1
        m = (max+min) // 2
        if l[m] < x:
            min = m+1
        elif l[m] > x:
            max = m-1
        else:
            return m

print bin_srch(l, 34)
        
         
