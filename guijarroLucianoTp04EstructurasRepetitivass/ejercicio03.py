num1 = int(input("Por favor ingrese un numero: "))
num2 = int(input("Por favor ingrese un segundo numero: "))
suma = 0

for i in range(num1+1, num2):
    suma = suma + i
print(suma)