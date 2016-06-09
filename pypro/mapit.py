import webbrowser, sys
if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    pass

webbrowser.open('https://www.google.com/maps/place/870+Valencia+St+San+Francisco+CA/')
