s = raw_input("enter: ")
letters  = 0
digits = 0
spaces = 0
others = 0
for i in s:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1
    else:
        others += 1

print "letters" , letters
print "digits" , digits
print "spaces" , spaces
print "others" , others
