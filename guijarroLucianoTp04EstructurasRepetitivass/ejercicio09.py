#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor)
CANTIDAD_DE_NUMEROS = 10
contador = 0


for i in range(0, CANTIDAD_DE_NUMEROS):
    num = int(input("Por favor ingresa un numero: "))
    contador = contador + num

print(f"La media de esos numeros es de {contador / CANTIDAD_DE_NUMEROS}")