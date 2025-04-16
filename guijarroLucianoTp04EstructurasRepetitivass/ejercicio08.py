#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numPares = 0
numImpares = 0
numPositivos = 0
numNegativos = 0

for i in range(0, 100 + 1):
    num = int(input("Por favor ingrese un numero: "))
    if num % 2 == 0 and num > 0:
        numPares += 1
        numPositivos +=1
    elif num % 2 != 0 and num > 0:
        numImpares +=1
        numPositivos +=1
    elif num < 0 and num % 2 == 0:
        numNegativos += 1
        numPares += 1
    elif num < 0 and num % 2 != 0:
        numNegativos += 1
        numImpares +=1


print(f"En esos numeros hay:\n {numPares} numeros pares\n {numImpares} numeros impares\n {numNegativos} numeros negativos\n {numPositivos} numeros positivos")