

#sum of ascii values of characters in a string


str = raw_input('enter the string:')

ascii_numbers = [ord(c) for c in str]

print ascii_numbers

print sum(ascii_numbers)

        
            
