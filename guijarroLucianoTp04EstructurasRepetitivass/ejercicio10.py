#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Por favor ingresa un numero: ")
numeroInvertido = numero[::-1]

print(numeroInvertido)