from tkinter import Tk, Frame, Button, messagebox, StringVar, Label, Entry
from mainh12 import *

objecto = Humano()

#metodos para mensajes
def mostrarMensajes():
    if nombre.get() == "" or contrasena.get() == "":
            print(messagebox.showinfo('showinfo', 'Tus credenciales estan correctas'))
    else:
            print(messagebox.showwarning('showwarning', 'Incorrecto'))

#1.Creamos la ventana
ventana= Tk() #Uso de POO creando un objeto ventana
ventana.title('Login')
ventana.geometry('600x400')



nombre = StringVar()
contrasena = StringVar()


Label(ventana, text="Nombre de usuario").pack()
Entry(ventana, textvariable=nombre).pack()

Label(ventana, text="Contraseña").pack()
Entry(ventana, textvariable=contrasena, show='*').pack()


seccion1= Frame(ventana, bg='black')
seccion1.pack(expand=True, fill='both')

botonValidar= Button(seccion1, text='Validar', fg='black', command=mostrarMensajes)
botonValidar.place(x=100, y=60, width=150, height=30)
botonValidar.pack()
    
    
    

#Ejecuta 
ventana.mainloop()