def factura(cantidad_no_iva, porcentaje_iva=21):
    iva = cantidad_no_iva * (porcentaje_iva / 100)
    total = cantidad_no_iva + iva
    return total

def main():
    cantidad_no_iva = float(input("cantidad sin: "))
    porcentaje_iva = float(input("porcentaje (Enter 21%): ") or 21)
    iva = factura(cantidad_no_iva, porcentaje_iva)
    print(f"El total es: {iva}")

main()