import re
beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('Hello there!')
print(mo)
endsWithWorldRegex = re.compile(r'world!$')
mo = endsWithWorldRegex.search('Hello world!')
print(mo)
allDigitsRegex = re.compile(r'^\d+$') #'^'-> empieza con - '$' -> termina con (string completo)
mo = allDigitsRegex.search('123x23') # '123x23' devuelve None
print(mo)
atRegex = re.compile(r'.at') # '.' Cualquier caracter menos 'space' 'nueva linea'(saltos de linea)
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)
name = 'First name: Daniel Last name: Benitez'
nameRegex = re.compile(r'First name: (.*) Last name: (.*)') # (.*) ->'dot star' cualquier conjunto 
mo = nameRegex.findall(name)                                # de caracteres
print(mo)

#hay dos tipos (.*) -> 'greedy'(mayor cant. de .) y (.*?) -> 'non-greedy'(menor cant. de .)
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
greedy = re.compile(r'<(.*)>')
print(nongreedy.findall(serve)) #ejemplo de <non-greedy>
print(greedy.findall(serve))    #ejemplo de <greedy>

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL) # re.DOTALL incluye a los saltos de linea
print(dotStar.search(prime))

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al, why does your programming book talk about Robocop so much?'))
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) #el segundo argumento hace al emparejamiento NO-Sensitivo
print(vowelRegex.findall('Al, why does your programming book talk about Robocop so much?'))
vowelRegex = re.compile(r'[aeiou]', re.I) #el segundo argumento hace al emparejamiento NO-Sensitivo
print(vowelRegex.findall('Al, why does your programming book talk about Robocop so much?'))