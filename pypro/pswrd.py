import re
l = []
psd = [x for x in raw_input("enter: ").split()]
for p in psd:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[$@#]", p): 
        continue
    else:
        pass
    l.append(p)

print ",".join(l)
