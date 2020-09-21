import pprint
lista = [
    110,
    50,
    9,
    89,
    5,
    1000
]

def ordenar(lista):
    i = 0   # la lista comienza con indice cero
    while i<len(lista)-1:   #se realizan el bloque de abajo hasta que el indice sea igual a la longitud de la lista
        if lista[i]<lista[i+1]: #si el valor siguiente es mayor
            lista[i], lista[i+1] = lista[i+1], lista[i] #se intercambian valores
            i = 0  #se comienza a iterar de nuevo
        else:
            i = i + 1   #de otra forma se evalua el siguiente valor
    return lista

print(lista)
ordenar(lista)
print(lista)