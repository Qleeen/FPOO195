menu= int(input('1. Convertir a Farenheit\n2. Convertir a Kelvin\n3. Salir'))
while menu != 3:
    if menu == 1:
        celsius = float(input('Ingrese la temperatura en grados Celsius: '))
        farenheit = (celsius * 9/5) + 32
        print('La temperatura es de', farenheit, 'grados Farenheit')
    elif menu == 2:
        celsius = float(input('Ingrese la temperatura en grados Celsius: '))
        kelvin = celsius + 273.15
        print('La temperatura es de', kelvin, 'grados Kelvin')
    else:
        print('Opcion no valida')
    menu= int(input('1. Convertir a Farenheit\n2. Convertir a Kelvin\n3. Salir'))
    
    
print('Adios')