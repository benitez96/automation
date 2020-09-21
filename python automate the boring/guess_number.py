import random
print('Hola jugador, cual es tu nombre?: ')
nombre = input()
numSecreto = random.randint(0, 20)
print(f'Bueno {nombre}, adivina en que numero estoy pensando(entre 0-20)')

for intentos in range(1,7):
    print('Tu respuesta es:')
    try:
        intento = int(input())
    except ValueError:
        print('Debes ingresar un numero!')
        continue
    if isinstance(intento, int):
        if intento < numSecreto:
            print('El numero que elegiste es muy chico.')
        elif intento > numSecreto:
            print('El numero que elegiste es muy alto')
        else:
            print('Correcto! Has ganado!!!')
            break
if intento == numSecreto:
    print(f"""
Correcto, estaba pensando en el {numSecreto}.
Te ha llevado {intentos} intentos ganar.""")
else:
    print(f'Has perdiodo =( . Estaba pensando en el {numSecreto}')
