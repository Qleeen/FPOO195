
def area_circulo(radio):
    return 3.1416*radio**2
def main():
    radio_circulo=float(input('ingrese valor del radio:'))
    area_result=area_circulo(radio_circulo)
    print(f'area del circulo:{area_result}')
main()

def volumen_cilindro(radio,altura):
    return 3.1416*radio**2*altura
def main():
    radio_cilindro=float(input('ingrese valor del radio:'))
    altura_cilindro=float(input('ingrese valor de la altura:'))
    print(f'volumen del cilindro:{volumen_cilindro(radio_cilindro,altura_cilindro)}')
main()
    
    