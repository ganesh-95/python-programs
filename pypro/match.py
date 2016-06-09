import re
s  = raw_input("enter: ")
x = "(\w+)@((\w+).(com))"
r = re.match(x,s)

print r.group(1)
print r.group(2)
print r.group(3)
print r.group(4)
