# 35 heads and 94 legs. how many chickens and rabbits are there?

def solve(h,l):
    for i in range(h):
        j = h-i
        if i*2 + 4*j == l:
            return i,j

print solve(35,94)
