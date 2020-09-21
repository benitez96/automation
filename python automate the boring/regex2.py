import re
batmanregex = re.compile(r'(bati)(movil|cueva|llamad[ao])')
mensaje = 'Batman acudio a la batillamada con el batimovil en 50 segundos'
mo = batmanregex.search(mensaje)
print(batmanregex.findall(mensaje))
print(mo.group())