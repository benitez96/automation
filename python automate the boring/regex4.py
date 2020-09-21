import re, pprint
lyrics = '''On the twelfth day of Christmas
my true love sent to me:
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree'''

xmasRegex = re.compile(r'\d+\s+\w+')
mf = xmasRegex.findall(lyrics)
pprint.pprint(mf)
print('----------------------')

doblevowels = re.compile(r'[aeiou]{2}') # equals to (r'(a|e|i|o|u)') --> {2} two vowes in a row
mf = doblevowels.findall('Robocop eats baby food')
print(mf)
print('----------------------')

consonantsRegex = re.compile(r'[^aeiouAEIOU]') # ^ negacion --> es decir se imprimen solo consonantes
mf = consonantsRegex.findall('Robocop eats baby food')
print(mf)