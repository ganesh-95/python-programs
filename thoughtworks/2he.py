
a = input()
b = input()

def intersect(a, b):
    return list(set(a) & set(b))
def union(a, b):
    return list(set(a) | set(b))

print intersect(a, b)
print union(a, b)
