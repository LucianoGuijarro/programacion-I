#Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Por favor indica en que hemisferio estas utilizanda S para sur y N para norte. ")
mes = int(input("Ingresa el numero del mes en el que estas. "))
dia = int(input("Ingresa el dia (en numero) en el que estas. "))

if hemisferio.lower() == "s":
    hemisferio = "sur"
elif hemisferio.lower() == "n":
    hemisferio = "norte"
else:
    print("Lo siente ingresaste un hemisferio invalido")

if hemisferio == "sur":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Es Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Es Otoño")
    elif (mes == 5 and dia >= 21) or (mes == 6) or (mes == 7) or (mes == 9 and dia <= 20):
        print("Es invierno")
    elif(mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Es primavera")

if hemisferio == "norte":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Es invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Es Primavea")
    elif (mes == 5 and dia >= 21) or (mes == 6) or (mes == 7) or (mes == 9 and dia <= 20):
        print("Es Verano")
    elif(mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Es Otoño")


