from tkinter import Tk, Frame, Button, StringVar, Label, Entry, Checkbutton, IntVar, messagebox
from clase import contraseña

# Creamos la ventana
ventana = Tk()
ventana.title('Generador de Contraseñas')
ventana.geometry('600x400')

# Variables para almacenar la longitud, mayúsculas y caracteres especiales
contrasena = StringVar()
mayusculas_var = IntVar()
caracteres_var = IntVar()

# Etiqueta para la longitud
Label(ventana, text="Longitud").pack()
Entry(ventana, textvariable=contrasena, show='*').pack()

# Casilla para incluir mayúsculas
Checkbutton(ventana, text="Incluir Mayúsculas", variable=mayusculas_var).pack()

# Casilla para incluir caracteres especiales
Checkbutton(ventana, text="Incluir Caracteres Especiales", variable=caracteres_var).pack()

# Sección de la interfaz
seccion1 = Frame(ventana, bg='white')
seccion1.pack(expand=True, fill='both')

def generar_contraseña():
    try:
        longitud = int(contrasena.get())
        incluir_mayusculas = bool(mayusculas_var.get())
        incluir_caracteres = bool(caracteres_var.get())
        
        mi_contraseña = contraseña(longitud, incluir_mayusculas, incluir_caracteres)
        nueva_contraseña = mi_contraseña.generar_contraseña()
        messagebox.showinfo("Contraseña Generada", f"Contraseña generada: {nueva_contraseña}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa una longitud válida (número entero)")

# Botón para generar contraseña
botonGenerar = Button(seccion1, text='Generar Contraseña', fg='black', command=generar_contraseña)
botonGenerar.place(x=100, y=60, width=150, height=30)
botonGenerar.pack()

# Ejecuta la ventana
ventana.mainloop()