
contraseña_guardada = "Contraseña"

contraseña_usuario = input("Ingrese la contraseña: ")

if contraseña_usuario.lower() == contraseña_guardada.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")



entero= int(input('Introduce un número entero'))
if entero % 2 == 0:
    print('entero es par')
else:
    print('entero es impar')
    
    
palabra = input('Introduce una serie de caracteres').lower().replace(' ', '')
if palabra == palabra[::-1]:
    print('La palabra es un palíndromo')
else:
    print('La palabra no es un palíndromo') 
    
edad= int(input('Introduce tu edad')) 
if edad < 4:
    print('La entrada es gratis')
elif edad >= 4 and edad <= 18:
    print('El precio de la entrada es 110$')
else:
    print('El precio de la entrada es 190$')
