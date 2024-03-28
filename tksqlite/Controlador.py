from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    def conexion(self):
        try:
            conex=sqlite3.connect("/Users/baru/Documents/5to cuatri/POO/Github/FPOO195/tksqlite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se puede conectar")
            
    def encriptapass(self,cont):
        passPlana = cont
        PassPlana = passPlana.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(PassPlana,sal)
        
        return passHash
    
    def insertUsuario(self,nom,corr,cont):
        conexion=self.conexion()
        
        if(nom=="" or corr=="" or cont==""):
            messagebox.showwarning("Cuidado","Inputs vacios menso")
            conexion.close()
            
        else:
            cursor = conexion.cursor()
            conH=self.encriptapass(cont)
            datos = (nom,corr,conH)
            sqlInsert ="insert into tbUsuarios(nombre,correo,contrasena) values(?,?,?)"
            
            
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito","Usuario guardado")
    
    def buscarUsuario(self,id):
        conex=self.conexion()
        if(id==""):
            messagebox.showwarning("Cuidado","Input vacio")
            conex.close()
        else:
            try:
                cursor = conex.cursor() 
                sqlSelect = "select * from tbusuarios where id=" + id  
                cursor.execute(sqlSelect)
                usuario=cursor.fetchall()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se puede ejecutar la busqueda")
        

                
    def mostrarUsuarios(self):
        conex = self.conexion()
        try:
            cursor = conex.cursor()
            sqlSelect = "select * from tbUsuarios"
            cursor.execute(sqlSelect)
            usuarios = cursor.fetchall()
            conex.close()
            return usuarios
        except sqlite3.OperationalError:
            print("No se puede ejecutar la consulta")