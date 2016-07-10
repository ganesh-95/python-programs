
#finding most and least occuring element in the given string

str = raw_input('enter the string:')

max_letter = str[0]
min_letter = str[0]

max = str.count(str[0])
min = str.count(str[0])

for c in str:
    if c is not ' ' and '.':
        if str.count(c) > max:
            max_letter = c
            max = str.count(c)
        if str.count(c) < min:
            min_letter = c
            min = str.count(c)


print max, max_letter
print min, min_letter
