from Persona import *

objectPeople= Persona

nombre = input("Escribe el nombre: ")
apellidoPaterno = input("Escribe el apellido paterno: ")
apellidoMaterno = input("Escribe el apellido materno: ")
añoNacimiento = int(input("Escribe el año de nacimiento: "))
Carrera = input("Escribe la carrera: ")
AñoCurso = int(input("Escribe el año de curso: "))
persona = Persona(AñoCurso, añoNacimiento, nombre, apellidoPaterno, apellidoMaterno, Carrera)
print("La matricula es: ", persona.generarMatricula())



