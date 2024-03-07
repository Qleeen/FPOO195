from tkinter import Tk, Button, Entry, Label, StringVar


ventana= Tk()
ventana.title('Login')
ventana.geometry('300x200')


nombre = StringVar()
contrasena = StringVar()

Label(ventana, text="Nombre de usuario").pack()
Entry(ventana, textvariable=nombre).pack()

Label(ventana, text="Contraseña").pack()
Entry(ventana, textvariable=contrasena, show='*').pack()

ventana.mainloop()