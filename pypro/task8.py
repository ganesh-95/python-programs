'''
Take user input until user enter correct option. Example: => Please Enter[Y/N]. if user enter "t" you have to display message "Please Enter correct option [Y/N]" until the input is "Y"/"N". Note: Use while.

'''

x = raw_input('please enter [Y/N]: ')

while not(x=='Y' or x=='N'):
    x = raw_input('enter valid option:')

print 'valid'
    
    



