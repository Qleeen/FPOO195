factura=float(input("Ingrese la cantidad: "))
iva=float(input("Ingrese el iva: "))
if iva == factura:
    iva*factura
else:
    iva*0.21

print(factura+iva)

