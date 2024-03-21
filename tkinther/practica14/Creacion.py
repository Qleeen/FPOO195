import random

class Crud:
    def __init__(self):
        self.__usuarios = []
        
  
    def generarCuenta(self):
        cuenta = ''.join(random.choices('123456789ABCDEFGHIJKLMNOPQRSTUBXYZ', k=18))
        return cuenta
    

    def buscarUsuarioPorCuenta(self,cuenta):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                return usuario['Titular']
        return None
    
    def getNombreUsuario(self,cuenta):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                return usuario['Titular']
        return None
    
    def getRegistros(self):
        return self.__usuarios
    
    def consultarCuentas(self):
        cuentas = []
        print('Lista de cuentas registradas:')
        for usuario in self.getRegistros():
            cuentastr = 'Cuenta: {}, Titular: {}, Edad: {}, Saldo: {}'.format(usuario['Cuenta'], usuario['Titular'],usuario['Edad'],usuario['Saldo'])
            print(cuentastr)
            cuentas.append(cuentastr)
        return cuentas
    
    def crearUsuario(self,titular,edad,saldo=0):
        cuenta = self.generarCuenta()
        while self.buscarUsuarioPorCuenta(cuenta):
            cuenta = self.generarCuenta()
            
        usuario = {
            'Cuenta':cuenta,
            'Titular':titular,
            'Edad':int(edad),
            'Saldo':float(saldo)
        }
        self.__usuarios.append(usuario)
        print('El usuario con los datos: '+ str(usuario) + ' fue registrado')
        return cuenta,saldo
        
    def getSaldo(self,cuenta):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                print('El saldo de la cuenta es: ', usuario['Saldo'])
                return usuario['Saldo']
        return None
        
    def ingresarEfectivo(self,cuenta,monto):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                saldoActual = usuario['Saldo']
                nuevoSaldo = saldoActual + monto
                usuario['Saldo'] = nuevoSaldo
                print('Se ingeso un monto de: ', monto, 'de la cuenta: ',cuenta)
                print('El saldo anterio era de: ',saldoActual, 'El nuevo saldo es: ',nuevoSaldo)
                return
        print('No existe la cuenta')
        
    def retirarEfectivo(self,cuenta,monto):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                if usuario['Saldo'] < monto:
                    print('El saldo de la cuenta: ',cuenta, 'no es suficiente para retirar')
                    return
                saldoActual = usuario['Saldo']
                nuevoSaldo = saldoActual - monto
                usuario['Saldo'] = nuevoSaldo
                print('Se retiro un monto de: ', monto, 'de la cuenta: ',cuenta)
                print('El saldo anterio era de: ',saldoActual, 'El nuevo saldo es: ',nuevoSaldo)
                return
            
        print('No existe la cuenta.')
            
    def transferencia(self,cuentaOrigen,cuentaDestino,monto):
                usuarioOrigen = None
                usuarioDestino = None
                
                for usuario in self.__usuarios:
                    if usuario['Cuenta'] == cuentaOrigen:
                        usuarioOrigen = usuario
                    elif usuario['Cuenta'] == cuentaDestino:
                        usuarioDestino = usuario
                        
                if usuarioOrigen is None:
                    print('No se encointro la cuenta de origen', cuentaOrigen)
                    return
                if usuarioDestino is None:
                    print('La cuenta de destino no se encontro', cuentaDestino)
                    return
                
                if usuarioOrigen['Saldo'] < monto:
                    print('La cuenta: ',cuentaOrigen, 'no cuenta con el saldo suficiente para transferir')
                    return
                usuarioOrigen['Saldo'] -= monto
                usuarioDestino['Saldo'] += monto
                
                print("Transferencia exitosa de", monto, "de la cuenta", cuentaOrigen, "a la cuenta", cuentaDestino)
                print("Nuevo saldo de la cuenta", cuentaOrigen, "es:", usuarioOrigen['Saldo'])
                print("Nuevo saldo de la cuenta", cuentaDestino, "es:", usuarioDestino['Saldo'])
                return cuentaOrigen, cuentaDestino, monto
