
num = int(input('Introduce un número entero positivo: '))

for i in range(1, num + 1, 2):
    
    print(i, end=', ')

num = int(input('Introduce un número entero positivo: '))
for i in range(num, -1, -1):
    print(i, end=', ')

for multiplo in range(1, 10):
    for multiplo in range(1, 10):
        print(f'{multiplo} x {multiplo} = {multiplo * multiplo}')


saldo = 0
num_operaciones = int(input("Escriba el número de operaciones: "))

for _ in range(num_operaciones):
    s = input("Escriba la bitacora de operaciones: ")
    datos = s.split(" ")
    operacion = datos[0]
    monto = int(datos[1])
    if operacion=="D":
        saldo+=monto
    elif operacion=="R":
        saldo-=monto
    else:
        pass

print (saldo)