s = raw_input("enter: ")
y = [i for i in s.split(',') if int(i) % 2 != 0]
print ",".join(y)
