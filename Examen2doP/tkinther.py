from tkinter import Tk, Frame, messagebox, Button
from Persona import *

ventana = Tk()
ventana.title('Generador de Matricula')
ventana.geometry('600x400')


seccion1 = Frame(ventana, bg='white')
seccion1.pack(expand=True, fill='both')

def generar_matricula():
    nombre = input("Escribe el nombre: ")
    apellidoPaterno = input("Escribe el apellido paterno: ")
    apellidoMaterno = input("Escribe el apellido materno: ")
    añoNacimiento = int(input("Escribe el año de nacimiento: "))
    Carrera = input("Escribe la carrera: ")
    AñoCurso = int(input("Escribe el año de curso: "))
    persona = Persona(AñoCurso, añoNacimiento, nombre, apellidoPaterno, apellidoMaterno, Carrera)
    print("La matricula es: ", persona.generarMatricula())
    

botonGenerar = Button(seccion1, text='Generar Matricula', fg='black', command=generar_matricula)
botonGenerar.place(x=100, y=60, width=150, height=30)
botonGenerar.pack()

ventana.mainloop()