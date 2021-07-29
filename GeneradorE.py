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


maxAcordes = 8
contadorAcordes = 0
escala = getEcala(0)

for i in escala:
    contadorAcordes += 1
    if (contadorAcordes == maxAcordes):
        break
    print(nombreNotas[i % 12])

contadorAcordes = 0
for notaRaiz in escala:
    contadorAcordes += 1
    if (contadorAcordes == maxAcordes):
        break
    print("Acorde # "+str(contadorAcordes))
    getAcorde(escala.index(notaRaiz), escala)
