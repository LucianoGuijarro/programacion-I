#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#n 0.
suma = 0
numero = int(input("Por favor ingresa un numero: "))

while numero != 0:
    suma = suma + numero
    numero = int(input("Por favor ingresa otro numero: "))

print(f"El resultado de esos numeros sumados es de {suma}")

