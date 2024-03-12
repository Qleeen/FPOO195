from Persona import *

objectPeople= Persona

nombre = input("Escribe el nombre: ")
apellidoPaterno = input("Escribe el apellido paterno: ")
apellidoMaterno = input("Escribe el apellido materno: ")
añoNacimiento = int(input("Escribe el año de nacimiento: "))
Carrera = input("Escribe la carrera: ")
AñoCurso = int(input("Escribe el año del curso: "))
persona = Persona(nombre, apellidoPaterno, apellidoMaterno, añoNacimiento, Carrera, AñoCurso)
print("Matricula: ", persona.generarMatricula())

