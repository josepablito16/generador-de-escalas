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

    print(nombreNotas[escala[notaRaiz] % 12])
    print(nombreNotas[escala[notaRaiz + 2] % 12])
    print(nombreNotas[escala[notaRaiz + 4] % 12])
    print()


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

# Se imprime nombres de la escala
print("Escala:")
for i in escala:
    contadorAcordes += 1
    if (contadorAcordes == maxAcordes):
        break
    print(nombreNotas[i % 12])

# Se imprime Acordes
print("\nAcordes:")
contadorAcordes = 0
for notaRaiz in escala:
    contadorAcordes += 1
    if (contadorAcordes == maxAcordes):
        break
    print("Acorde # "+str(contadorAcordes))
    getAcorde(escala.index(notaRaiz), escala)
