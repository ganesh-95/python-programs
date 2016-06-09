s = raw_input("enter sentence: ")
print " ".join(sorted(list(set(x for x in s.split()))))
