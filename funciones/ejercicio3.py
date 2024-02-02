
def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def main():
    numero_decimal = int(input('Ingrese el valor del número: '))
    binario_result = decimal_a_binario(numero_decimal)
    print(f'Número binario: {binario_result}')
main()



def binario_a_decimal(binario):
    return int(binario, 2)
def main():
    numero_binario = input('Ingrese el valor del número binario: ')
    decimal_result = binario_a_decimal(numero_binario)
    print(f'Número decimal: {decimal_result}')
main()



