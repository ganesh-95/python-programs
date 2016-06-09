s = raw_input("enter: ")
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    else:
        pass

print "upper" , upper
print "lower" , lower
