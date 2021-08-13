formulaEscalaMayor = [2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1]
nombreNotas = ['Do', 'DO#', 'RE', 'RE#', 'MI',
               'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI']


def getEcala(notaInicial):
    escala = []
    notaActual = notaInicial
    escala.append(notaActual)
    for salto in formulaEscalaMayor:
        notaActual += salto
        escala.append(notaActual)
    return escala


def getAcorde(notaRaiz, escala):
    return [nombreNotas[escala[notaRaiz] % 12],
            nombreNotas[escala[notaRaiz + 2] % 12],
            nombreNotas[escala[notaRaiz + 4] % 12]]


def getClaseAcorde(acorde):
    nota1 = nombreNotas.index(acorde[0])
    nota2 = nombreNotas.index(acorde[1])
    nota3 = nombreNotas.index(acorde[2])

    rango1 = abs(nota2 - nota1)
    rango2 = abs(nota3 - nota2)

    if(rango1 == 9):
        rango1 = 3

    if(rango2 == 9):
        rango2 = 3

    # clasificacion de acordes
    if(rango1 == 4 and rango2 == 3):
        print(f"{acorde[0]} Mayor")

    if(rango1 == 3 and rango2 == 4):
        print(f"{acorde[0]} Menor")

    if(rango1 == 3 and rango2 == 3):
        print(f"{acorde[0]} Disminuido")

    if(rango1 == 4 and rango2 == 4):
        print(f"{acorde[0]} Aumentado")


print('''
0. Primer Grado
1. Segundo Grado
2. Tercer Grado
3. Cuarto Grado
4. Quinto Grado
5. Sexto Grado
6. Septimo Grado
''')

gradoIndex = int(input("Escriba el numero de grado: "))

print('''
0. Do
1. DO#
2. RE
3. RE#
4. MI
5. FA
6. FA#
7. SOL
8. SOL#
9. LA
10. LA#
11. SI
''')

notaIndex = int(input("Escriba el numero de nota: "))

maxAcordes = 8
contadorAcordes = 0
escala = getEcala(notaIndex)

# Se imprime Acordes
print("\nAcorde:")

acorde = getAcorde(gradoIndex, escala)
getClaseAcorde(acorde)
print('-'.join(acorde))


if (gradoIndex == 0 or gradoIndex == 2 or gradoIndex == 5):
    print("Funcion Tonal: Tonica")

elif (gradoIndex == 1 or gradoIndex == 3):
    print("Funcion Tonal: Subdominante")

elif (gradoIndex == 4 or gradoIndex == 6):
    print("Funcion Tonal: Dominante")
