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