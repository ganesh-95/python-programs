l = []
items = [x for x in raw_input("enter the binary: ").split(',')]
for p in items:
    x = int(p, 2)
    if not x%5:
        l.append(p)
print ','.join(l)
        
