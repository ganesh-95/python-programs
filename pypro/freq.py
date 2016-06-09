s = raw_input("enter: ").split(" ")
count = {}
for word in s:
    count[word] = count.get(word,0)+1
words = count.keys()
words.sort()

for w in words:
    print "%s: %d" % (w, count[w])
