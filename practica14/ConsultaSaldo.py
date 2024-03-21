import tkinter as tk
from tkinter import messagebox
from Creacion import Crud

class ConsultaSaldo:
        def __init__(self, ventana, crud):
            self.ventana = ventana
            self.crud = crud
            self.ventana.title('Consulta  Saldo')
            self.ventana.geometry('800x500')

            fontStyleTitlle = ('Arial', 20,)
            fontStyleText = ('Arial', 12)
            labelStyle = {'font': fontStyleText, 'fg': 'black'}
            entryStyle = {'font': fontStyleText, 'fg': 'black'}
            buttonStyle = {'font': ('Arial', 12, 'bold'), 'bg': 'black', 'fg': 'black'}

            info = 'Ingrese la cuenta de la que se quiere saber el saldo'
            self.labelInfo = tk.Label(ventana, text=info, font=fontStyleTitlle)
            self.labelInfo.pack()

            self.labelCuenta = tk.Label(ventana, text='Cuenta a consultar el saldo: ', **labelStyle)
            self.labelCuenta.pack()

            self.entryCuenta = tk.Entry(ventana, **entryStyle)
            self.entryCuenta.pack()

            self.botonConsultar = tk.Button(ventana, text='Consultar', command=self.consultarSaldo, **buttonStyle)
            self.botonConsultar.pack()

            self.ventana.configure(bg='white')
            self.labelInfo.configure(bg='white')
            self.labelCuenta.configure(bg='white')
            self.botonConsultar.configure(bg='black')
            self.entryCuenta.configure(bg='white')
            self.botonConsultar.configure(fg='black')
            self.labelInfo.configure(fg='white')
            self.labelCuenta.configure(fg='white')
            self.ventana.geometry('800x500')
            fontStyleTitlle = ('Arial', 30, )
            self.labelInfo.configure(font=fontStyleTitlle)
            fontStyleText = ('Arial', 14)
            self.labelCuenta.configure(font=fontStyleText)
            self.botonConsultar.configure(font=('Arial', 14, ))

        def consultarSaldo(self):
            cuenta = self.entryCuenta.get()
            if cuenta == '':
                messagebox.showerror('Error', 'Falta ingresar datos')
                return
            saldo = self.crud.getSaldo(cuenta)
            titular = self.crud.getNombreUsuario(cuenta)
            if saldo is None:
                messagebox.showerror('Error', 'No existe la cuenta')
                return
            messagebox.showinfo('Saldo', f'El saldo de la cuenta {cuenta}, que pertenece a: {titular}, es: {saldo}')


if __name__ == '__main__':
        ventana = tk.Tk()
        crud = Crud()
        cuenta = crud.crearUsuario('Baru', 19, 0)
        app = ConsultaSaldo(ventana, crud)
