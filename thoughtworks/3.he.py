


a = input()

def find(arr):
    for x in range(1,len(arr)-1):
        if x not in arr:
            return x

print find(a)
    

