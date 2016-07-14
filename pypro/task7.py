'''
Display "wellcome" message when user enter correct password other wise print "wrong password. enter correct password". loop should terminate if user enter correct password. Note: use while. assume correct password as "git123"

'''

x = raw_input('enter password:')

correct_password = 'git123'

while x != correct_password:
    x = raw_input('wrong password. enter correct password: ')

print 'welcome'
