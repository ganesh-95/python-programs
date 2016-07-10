
#polindromes in a given string 

s = raw_input('enter:')

x  = s.split()


for word in x:
    if str(word) == str(word)[::-1]:
        print word
    

