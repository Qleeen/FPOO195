import tkinter as tk
from tkinter import messagebox
from Creacion import Crud

class Transferencia:
    def __init__(self, ventana,crud):
        self.ventana = ventana
        self.crud = crud
        self.ventana.title('Transferencia')
        self.ventana.geometry('800x500')



        fontStyleTitlle = ('Arial', 20, 'bold')

        fontStyleText = ('Arial', 12)
        labelStyle = {'font': fontStyleText, 'fg': 'black'}

        entryStyle = {'font': fontStyleText, 'fg': 'black'}


        buttonStyle = {'font': ('Arial', 12, 'bold'), 'bg': 'black', 'fg': 'black'}


        info = 'Ingrese los datos de la transferencia'
        self.labelInfo = tk.Label(ventana, text = info, font=fontStyleTitlle)
        self.labelInfo.pack()

        self.labelCuentaOrigen = tk.Label(ventana, text = 'Cuenta de origen: ', **labelStyle)
        self.labelCuentaOrigen.pack()

        self.entryCuentaOrigen = tk.Entry(ventana, **entryStyle)
        self.entryCuentaOrigen.pack()


        self.labelCuentaDestino = tk.Label(ventana, text = 'Cuenta de destino: ', **labelStyle)
        self.labelCuentaDestino.pack()

        self.entryCuentaDestino = tk.Entry(ventana, **entryStyle)
        self.entryCuentaDestino.pack()


        self.labelMonto = tk.Label(ventana, text = 'Monto a transferir: ', **labelStyle)
        self.labelMonto.pack()

        self.entryMonto = tk.Entry(ventana, **entryStyle)
        self.entryMonto.pack()


        self.botonTransferir = tk.Button(ventana, text = 'Transferir', command=self.transferir, **buttonStyle)
        self.botonTransferir.pack()
        
    def transferir(self):
        cuentaOrigen = self.entryCuentaOrigen.get()
        cuentaDestino = self.entryCuentaDestino.get()
        monto = float(self.entryMonto.get())
        if cuentaOrigen == '' or cuentaDestino == '' or monto <= 0:
            messagebox.showerror('Error', 'Verifique que los campos esten llenos y que el monto sea mayor a 0.')
            return
        
        #tratamiento de errores
        saldoCuentaOrigen = self.crud.getSaldo(cuentaOrigen)
        existencuentaOrigen = self.crud.buscarUsuarioPorCuenta(cuentaOrigen)
        existenciaCuentaDestino = self.crud.buscarUsuarioPorCuenta(cuentaDestino)
        if existenciaCuentaDestino is None:
            messagebox.showerror('Error', f'No existe la cuenta de destino: {cuentaDestino}')
            return
        if existencuentaOrigen is None:
            messagebox.showerror('Error', f'No existe la cuenta de origen: {cuentaOrigen}')
            return
        if saldoCuentaOrigen < monto:
            messagebox.showerror('Error', f'La cuenta de origen: {cuentaOrigen} no cuenta con el saldo suficiente para transferir.')
            return
        
        co,cd,m = self.crud.transferencia(cuentaOrigen, cuentaDestino, monto)
        saldoNuevoCuentaOrigen = self.crud.getSaldo(co)
        saldoNuevoCuentaDestino = self.crud.getSaldo(cd)
        nombreCuentaOrigen = self.crud.buscarUsuarioPorCuenta(co)
        nombreCuentaDestino = self.crud.buscarUsuarioPorCuenta(cd)
        mensaje = f'Se ha transferido el monto de: {m} de la cuenta: {co} que pertenece al usuario: {nombreCuentaOrigen}\n A la cuenta: {cd}, que pertenece al usuario: {nombreCuentaDestino}.\n\n'
        mensaje += f'Nuevo saldo de la cuenta {co}: {saldoNuevoCuentaOrigen}, perteneciente a: {nombreCuentaOrigen}\n'
        mensaje += f'Nuevo saldo de la cuenta {cd}: {saldoNuevoCuentaDestino}, perteneciente a: {nombreCuentaDestino}'

        messagebox.showinfo('Transferencia exitosa', mensaje)
        

        self.entryCuentaOrigen.delete(0, tk.END)
        self.entryCuentaDestino.delete(0, tk.END)
        self.entryMonto.delete(0, tk.END)
        self.entryCuentaOrigen.focus_set()
        
if __name__ == '__main__':
    ventana = tk.Tk()
    crud = Crud()
    app = Transferencia(ventana, crud)
    ventana.mainloop()
        