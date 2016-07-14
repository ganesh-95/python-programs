'''
 Take a string from key board and count no of spaces and no of words in that. Eg: When you run the code it should prompt like "Enter a sentence:" And then you can enter a sentence like Welcome to MicroPyramid. Output should be spaces: 2, words: 3

'''



x = raw_input('enter a sentense:')

count_words = 0

count_space = 0

for i in x:
    if i.isspace() :
        count_space += 1
    elif i.isalpha():
        count_words += 1

print count_space
print count_words
    
