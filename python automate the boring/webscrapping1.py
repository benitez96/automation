import webbrowser, sys, pyperclip


if len(sys.argv)>1:                     #sys.argv --> ['maping.py', 'calle', 'altrura', 'ciudad', 'etc.']
    adress = ' '.join(sys.argv[1:])     #Transform the list in a string.
else:
    adress = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/%s'  %(adress))

