import math
def area_cuadrado(lado):
    return lado**2
def main():
    lado_cuadrado=float(input('ingrese valor del lado:'))
    area_result=area_cuadrado(lado_cuadrado)
    print(f'area del cuadrado:{area_result}')
main()
    