#####EJEMPLOS DE SUMAR NUMEROS#######
import time

# Suma usando un bucle for
def suma_iterativa(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Suma usando la fórmula de Gauss
def suma_gauss(n):
    return n * (n + 1) // 2

# Medición de tiempo para cada método
n = 1000000

inicio = time.time()
resultado_iterativa = suma_iterativa(n)
fin = time.time()
print("Suma iterativa:", resultado_iterativa, "- Tiempo:", fin - inicio)

inicio = time.time()
resultado_gauss = suma_gauss(n)
fin = time.time()
print("Suma Gauss:", resultado_gauss, "- Tiempo:", fin - inicio)

####EJEMPLO DE RAICES CUADRADAS#####
import time
import math

def suma_raices(n):
    total = 0
    for i in range(1, n + 1):
        total += math.sqrt(i)
    return total

n = 100000

inicio = time.time()
resultado = suma_raices(n)
fin = time.time()
print("Suma de raíces:", resultado, "- Tiempo:", fin - inicio)

