'''
Take file name from keyboard and check if the entered file name is an 'mp3' file or not. Eg: When you run the script it will display like "Enter File Name:" then if the user enters abc.mp3 then it should say Valid file, otherwise it should ask for valid file until user enters a valid file name.

'''


x = raw_input('enter the file name:')

while not (x.endswith('.mp3')):
    x = raw_input('enter the valid file name:')

print 'valid file'
