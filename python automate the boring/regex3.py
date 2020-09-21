import re
# Repeticion en expresiones regulares
batRegex = re.compile(r'Bat(wo)?man') # '"(grupo)?" -> puede aparecer 0-1 vez'
mo = batRegex.search('The Adventures of Batman') # mo --> 'match object'
print(mo)
mo = batRegex.search('The Adventures of Batwoman')
print(mo)
phoneNumberRegex = re.compile(r'(\d\d\d\d)?(-)?\d\d\d\d\d\d')
mophone = phoneNumberRegex.search('My number is 3794557159, llamame mañana')
print(mophone)


batRegex = re.compile(r'Bat(wo)*man') # '"(grupo)*" -> puede aparecer 0-n veces'
mo = batRegex.search('The Adventures of Batwowowowowoman')
print(mo)

print('------------------------------')

batRegex = re.compile(r'Bat(wo)+man') # '"(grupo)+" -> puede aparecer 1-n veces'
mo = batRegex.search('The Adventures of Batwowowowowoman')
print(mo)

print('-----------------------------')

regex = re.compile(r'\+\*\?') #se usa backslash(\) para tomar los signos como literales
mo  = regex.search('I learned about +*? regular expresions')
print(mo)

print('---------------------------')

haRegex = re.compile(r'(Ha){3}') #'Ha' se repite 3 veces
mo = haRegex.search('He said HaHaHa')
print(mo)
print('----------------------------')
phoneNumberRegex = re.compile(r'((\d){4})?(-)?(\d){6}') 
mophone = phoneNumberRegex.search('My number is 3794-557159, llamame mañana')
print(mophone)
print('------------------')

digitRegex = re.compile(r'(\d){3,5}') # --> toma la cota superior
mo = digitRegex.search('123456789')
print(mo)
print('-------------------')
digitRegex = re.compile(r'(\d){3,5}?') # --> toma la cota inferior
mo = digitRegex.search('123456789')
print(mo)