l = [x for x in range(1000, 3001) if all(int(b) % 2 == 0 for b in str(x))]
print l




# method 2

l = []   
for i in range(1000, 3001):
    if all(int(a) % 2 == 0 for a in str(i)):
        l.append(i)

print l
