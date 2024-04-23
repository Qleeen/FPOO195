#ejercicio 4
ingreso = input("Ingrese un número de 3 dígitos: ")
while len(ingreso) != 3:
    ingreso = input("El número debe tener 3 dígitos: ")
suma = 0
for i in ingreso:
    suma += int(i)
print("La suma de los dígitos es:", suma)