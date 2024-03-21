import tkinter as tk
from tkinter import messagebox
from Creacion import Crud
from Saldo import ConsultaSaldo
from CrearUsuario import CrearUsuario
from Deposito import Deposito
from Retiro import Retiro
from Trans import Transferencia



class MainMenu:
        def __init__(self,ventana):
            self.ventana = ventana
            self.ventana.title('Banco.')
            self.ventana.geometry('800x500')
            self.creacion = Crud()
            fontStyleTitlle = ('Arial', 24, 'bold')
            buttonStyle = {'font': ('Arial', 12, 'bold'), 'bg': 'green', 'fg': 'black'}
            info = 'Menú Principal. \nBanco'
            self.labelInfo = tk.Label(ventana, text = info, font=fontStyleTitlle)
            self.labelInfo.pack()
            self.botonCrearUsuario = tk.Button(ventana, text = 'Crear Usuario', command=self.crearUsuario, **buttonStyle)
            self.botonCrearUsuario.pack()
            self.botonConsultar = tk.Button(ventana, text = 'Consultar Saldo', command=self.consultarSaldo, **buttonStyle)
            self.botonConsultar.pack()
            self.botonDepositar = tk.Button(ventana, text = 'Depositar', command=self.depositar, **buttonStyle)
            self.botonDepositar.pack()
            self.botonRetirar = tk.Button(ventana, text = 'Retirar', command=self.retirar, **buttonStyle)
            self.botonRetirar.pack()
            self.botonTransferir = tk.Button(ventana, text = 'Transferir', command=self.transferir, **buttonStyle)
            self.botonTransferir.pack()

        def consultarSaldo(self):
            ventana = tk.Toplevel(self.ventana)
            app = ConsultaSaldo(ventana,self.crud)

        def crearUsuario(self):
            ventana = tk.Toplevel(self.ventana)
            app = CrearUsuario(ventana,self.crud)

        def depositar(self):
            ventana = tk.Toplevel(self.ventana)
            app = Deposito(ventana,self.crud)

        def retirar(self):
            ventana = tk.Toplevel(self.ventana)
            app = Retiro(ventana,self.crud)

        def transferir(self):
            ventana = tk.Toplevel(self.ventana)
            app = Transferencia(ventana,self.crud)

            
if __name__ == '__main__':
        root = tk.Tk()
        app = MainMenu(root)
        root.mainloop()
