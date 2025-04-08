#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random
numeroRamdon = random.randint(0,9)
contador = 1
numero = int(input("Por favor adivinar el numero secreto (del 0 al 9): "))

while numeroRamdon != numero:
    if numero < 0 or numero > 9:
        contador += 1
        print("Asi no ganarás porque el numero está entre el 0 y el 9")
        numero = int(input("Oh no fallaste! Elige otro numero: "))
    else:
        contador += 1
        numero = int(input("Oh no fallaste! Elige otro numero: "))

print(f"Felicidaes! Adivinaste el numero en {contador} intentos.")
