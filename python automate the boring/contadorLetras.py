#! python3

import pprint #Libreria "Prety Print", realiza mejores impresiones por pantalla
message = 'aosidjqwpoeiqwekpoksdalsd'
count ={}
for i in message.upper():
    count.setdefault(i, 0) #si no existe la clave la agrega con valor 0
    count[i] = count[i] + 1 #si ya existe la clave, suma +1 al valor

pprint.pprint(count)
