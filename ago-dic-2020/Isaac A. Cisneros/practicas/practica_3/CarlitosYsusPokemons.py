import sys
line1 = input().split()
line2 = input().split()
cont = 0
print("Hola Carlitos, ingresa el número de Pokemons que has capturado y sus puntos de combate")
for i in range(0, len(line1)):
    if (int(line1[i]) > 50):
        sys.exit()
    cont += 1
if (cont > 1):
    sys.exit()
cont = 0
for i in range(0, len(line2)):
    if(int(line2[i]) > 2000):
        sys.exit()
    cont += 1
if(cont != int(line1[0])):
    sys.exit()
for i in range(1, len(line2)):
    actual = line2[i]
    indice = i

    while indice > 0 and int(line2[indice-1]) < int(actual):
        line2[indice] = line2[indice-1]
        indice = indice - 1

    line2[indice] = actual
print(line2)