# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”

notaAlumno = int(input("Por favor ingrese su nota: "))

if notaAlumno >= 6:
    print("Felicidades! Estas aprobado")
else:
    print("Lo siento! Estas desaprobado")