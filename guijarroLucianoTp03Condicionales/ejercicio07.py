#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

palabra = input("Por favor ingrese una palabra o una frase: ")
ultimaLetra = palabra[-1]

if ultimaLetra.lower() in "aeiou":
    print(f"{palabra}!")
else:
    print(palabra)

