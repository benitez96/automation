import re
namesRegex = re.compile(r'Agent (\w)\w+') # (\w)->grupo 1
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)
print(namesRegex.sub(r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.'))
#devuelve lo que hay en el grupo uno (en esta caso 'A' y 'B').

phoneRegex = re.compile(r'''
(\d\d\d-|           #area code(without parens and dash)
\(\d\d\d\))         # -or- area code(with parens) and no dash
\d\d\d              #first 3 digits
-                   #second dash
\d\d\d\d            #last 4 digits
(\sx\d{2,4})?         #extension like x1234
''', re.VERBOSE | re.IGNORECASE)        # ''Metodo VERBOSE permite realizar comentarios dentro de patrones.''
# 'Se pueden usar mas de 1 metodo utilizado bitwise (|).

print(phoneRegex.sub(r'***', 'My phone number is 011-555-0808 or (011)333-0808, call anytime you want'))