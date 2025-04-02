#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random

numerosAleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numerosAleatorios)
mediana = median(numerosAleatorios)
moda = mode(numerosAleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No hay ningun Sesgo")

