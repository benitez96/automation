import re

message = 'Podes llamarme al 3777-557159 (movil) o al 3777-451239 (fijo) cuando gustes.'
patern = re.compile(r'(\d\d\d\d)-(\d\d\d\d\d\d)') # Se crea un objeto expresion regular
mo = patern.findall(message) #Se busca en el texto la coincidencias con el patron
mo2 = patern.search(message) #Se crea un objeto  con la primer coincidencia
print(mo2.group()) # 'group' sirve para obtener el objeto (get)
print(mo)
print(mo2.group(1)) #codigo de area
print(mo2.group(2)) #numero