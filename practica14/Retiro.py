import tkinter as tk
from tkinter import messagebox
from Creacion import Crud

class Retiro:
    def __init__(self,ventana,crud):
        self.ventana = ventana
        self.crud = crud
        self.ventana.title('Retiro')
        self.ventana.geometry('800x500')
        

        fontStyleTitlle = ('Arial', 22, 'bold')

      
        fontStyleText = ('Arial', 15)
        labelStyle = {'font': fontStyleText, 'fg': 'black'}

        entryStyle = {'font': fontStyleText, 'fg': 'black'}

        buttonStyle = {'font': ('Arial', 15, 'bold'), 'bg': 'green', 'fg': 'black'}

        info = 'Ingrese datos para retirar efectivo.'
        self.labelInfo = tk.Label(ventana, text = info, font=fontStyleTitlle)
        self.labelInfo.pack()
        
        self.labelCuenta = tk.Label(ventana, text = 'Cuenta a la cual se va a retirar ', **labelStyle)
        self.labelCuenta.pack()
        
        self.entryCuenta = tk.Entry(ventana, **entryStyle)
        self.entryCuenta.pack()
        
        self.labelMonto = tk.Label(ventana, text = 'Monto a retirar: ', **labelStyle)
        self.labelMonto.pack()
        
        self.entryMonto = tk.Entry(ventana, **entryStyle)
        self.entryMonto.pack()
        
        self.botonDepositar = tk.Button(ventana, text = 'retirar', command=self.retirar, **buttonStyle)
        self.botonDepositar.pack()
        
    def retirar(self):
      cuenta = self.entryCuenta.get()
      monto_text = self.entryMonto.get()

      if cuenta == '':
        messagebox.showerror('Error', 'Falta ingresar la cuenta')
        return

      if monto_text == '':
        messagebox.showerror('Error', 'Falta ingresar el monto')
        return

      try:
          monto = float(monto_text)
      except ValueError:
          messagebox.showerror('Error', 'El monto debe ser un número válido')
          return

      if monto <= 0:
        messagebox.showerror('Error', 'El monto a retirar debe ser mayor a 0')
        return

      existenciaCuenta = self.crud.buscarUsuarioPorCuenta(cuenta)
      if existenciaCuenta is None:
        messagebox.showerror('Error', 'La cuenta no existe')
        return

      if monto > self.crud.getSaldo(cuenta):
        messagebox.showerror('Error', 'El monto a retirar es mayor al saldo de la cuenta')
        return
      self.crud.retirarEfectivo(cuenta, monto)
      saldoActual = self.crud.getSaldo(cuenta)
      titular = self.crud.getNombreUsuario(cuenta)
      mensajeRetiro = f'Se ha retirado el monto de {monto} de la cuenta {cuenta}.\n El nuevo saldo es: {saldoActual}\n\n'
      mensajeRetiro += f'El propietario de la cuenta es: {titular}'
      messagebox.showinfo('Retiro', mensajeRetiro)
      self.entryCuenta.delete(0, tk.END)
      self.entryMonto.delete(0, tk.END)
      self.entryCuenta.focus_set()

if __name__ == '__main__':
    ventana = tk.Tk()
    crud = Crud()
    app = Retiro(ventana,crud)
    ventana.mainloop()