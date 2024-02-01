hora= int(input('Introduce tus horas de trabajo')) 
costo= float(input('Introduce el costo por hora'))

paga= hora*costo
print('Tu pago es de', paga, 'pesos')

nom= str(input('Introduce tu nombre'))
apell= str(input('Introduce tus apellidos'))
print(nom.lower(), apell.lower())
print(nom.upper(), apell.upper())
print(nom[0:1], apell.upper())



x= int(input('Introduce un numero'))
s=0
for i in range(1, x+1):
    s= s+i
    print(s)
    
    
    
name= str(input('Introduce tu nombre'))
print(name.upper(),'Tiene', len(name), 'letras')


frase= str(input( 'Introduce una frase'))
fraseinv= frase[::-1]
print(fraseinv)


peso_payaso = 112
peso_muñeca = 75


num_payasos = int(input('Introduce el número de payasos vendidos: '))
num_muñecas = int(input('Introduce el número de muñecas vendidas: '))

peso_total = num_payasos * peso_payaso + num_muñecas * peso_muñeca

print('El peso total del paquete será de', peso_total, 'gramos')

