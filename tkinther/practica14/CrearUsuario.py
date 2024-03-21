import tkinter as tk
from tkinter import messagebox
from Creacion import Crud


class CrearUsuario:
    def __init__(self, ventana, crud):
        self.vetana = ventana
        self.crud = crud
        self.vetana.title('Crear Usuario')
        self.vetana.geometry('800x500')

        fontStyleTitlle = ('Arial', 12, 'bold')
        fontStyleText = ('Arial', 12)
        labelStyle = {'font': fontStyleText, 'fg': 'black'}
        entryStyle = {'font': fontStyleText, 'fg': 'black'}
        buttonStyle = {'font': ('Arial', 12, 'bold'), 'bg': 'black', 'fg': 'black'} 

        info = 'Ingrese los datos del propietario de la cuenta a crear'
        self.labelInfo = tk.Label(ventana, text=info, font=fontStyleTitlle)
        self.labelInfo.pack()

        self.labelNombre = tk.Label(ventana, text='Nombre : ', **labelStyle)
        self.labelNombre.pack()

        self.entryNombre = tk.Entry(ventana, **entryStyle)
        self.entryNombre.pack()

        self.labelEdad = tk.Label(ventana, text='Edad: ', **labelStyle)
        self.labelEdad.pack()

        self.entryEdad = tk.Entry(ventana, **entryStyle)
        self.entryEdad.pack()

        self.botonCrear = tk.Button(ventana, text='Crear Usuario', command=self.crearUsuario, **buttonStyle)
        self.botonCrear.pack()

    def crearUsuario(self):
        nombre = self.entryNombre.get()
        edad = self.entryEdad.get()
        if nombre == '' or edad == '':
            messagebox.showerror('Error', 'Faltan datos por ingresar')
            return

        cuenta, saldo = self.crud.crearUsuario(nombre, edad)
        mensajeRegistro = f'Se ha registrado el usuario :\n\n'
        mensajeRegistro += f'Nombre: {nombre}\n'
        mensajeRegistro += f'No. Cuenta: {cuenta}\n'
        mensajeRegistro += f'Edad: {edad} años\n'
        mensajeRegistro += f'Saldo: {saldo}\n'
        messagebox.showinfo('Exito', mensajeRegistro)

        self.entryNombre.delete(0, tk.END)
        self.entryEdad.delete(0, tk.END)
        self.entryNombre.focus_set()


if __name__ == '__main__':
    ventana = tk.Tk()
    crud = Crud()
    app = CrearUsuario(ventana, crud)
    ventana.mainloop()
