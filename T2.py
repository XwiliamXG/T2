import random
import math

def distancia(par):
    return math.sqrt(par[0]**2 + par[1]**2)

def mergeSort(coordenadas):
    if len(coordenadas) == 1:
        x, y = coordenadas[0]
        if x > 0 and y < 0:
            return coordenadas[0]
        else:
            return [-1, 1] 
    medio = len(coordenadas) // 2
    izq = []
    der = []
    for i in range(medio):
        izq.append(coordenadas[i])
    for i in range(medio, len(coordenadas)):
        der.append(coordenadas[i])
    sorted_izq = mergeSort(izq)
    sorted_der = mergeSort(der)
    return Comparar(sorted_izq, sorted_der)

def Comparar(PrimeraC, SegundaC):
    if PrimeraC[0] <= 0 or PrimeraC[1] >= 0:
        return SegundaC
    if SegundaC[0] <= 0 or SegundaC[1] >= 0:
        return PrimeraC
    return PrimeraC if distancia(PrimeraC) > distancia(SegundaC) else SegundaC

n = int(input("Ingrese la cantidad de coordenadas a generar: "))

coordenadas = []
for _ in range(n):
    x = random.randint(-81, 81)
    y = random.randint(-81, 81)
    coordenadas.append([x, y])

print("Coordenadas generadas son las siguientes:")
for par in coordenadas:
    print(par)

resultado = mergeSort(coordenadas)

if resultado[0] > 0 and resultado[1] < 0:
    print("La coordenada más alejada en el cuadrante 4 es:", resultado)
    print("Distancia del punto al origen:", distancia(resultado))
else:
    print("No hay coordenadas con X positivo e Y negativo.")

