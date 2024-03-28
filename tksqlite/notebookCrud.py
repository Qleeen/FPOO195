from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

# Llamamos a nuestra clase Controlador
objControlador = Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

def busUsuario():
   usuarioBd = objControlador.buscarUsuario(varBus.get())
   if usuarioBd == None:
       texto_salida = "No se encontró el usuario"
   else:
       texto_salida= str(usuarioBd)
       text_box.delete(1.0,END)
       text_box.insert(1.0,texto_salida)

def consultaUsuarios():
    usuarios = objControlador.mostrarUsuarios()
    texto_salida = ""
    for usuario in usuarios:
        texto_salida += str(usuario) + "\n"
    text_box_consulta.delete(1.0,END)
    text_box_consulta.insert(1.0,texto_salida)
    
    
#1 crear la ventana
Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

#2. preparar el notebook para pestañas
panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

#3. Pestañas que ocuparemos para el panel
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

#4 Agregaremos las pesatañas que queremos crear al panel
panel.add(pestana1, text="Crear Usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Editar Usuario")
panel.add(pestana5, text="Eliminar Usuario")

#5. Formulario de Insert 
Label(pestana1, text="Registro de Usuarios", fg="blue", font=("Modern", 18)).pack()

var1 = tk.StringVar()
Label(pestana1, text="Nombre:").pack()
Entry(pestana1, textvariable=var1).pack()

var2 = tk.StringVar()
Label(pestana1, text="Correo:").pack()
Entry(pestana1, textvariable=var2).pack()

var3 = tk.StringVar()
Label(pestana1, text="Contrasena:").pack()
Entry(pestana1, textvariable=var3).pack()

# En el button de guardar usuario colocaremos el comando que realizara todo el proceso del usuario
Button(pestana1, text="Guardar usuario", command=ejecutaInsert).pack()

#6 Pestaña 2: Buscar usuario
Label(pestana2, text="Buscar Usuario", fg="black", font=("Modern", 18)).pack()

varBus = tk.StringVar()
Label(pestana2, text="Id:").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2, text="Buscar Usuario", command=busUsuario).pack()

text_box = tk.Text(pestana2, height=5, width=52)
text_box.pack()

#7 Pestaña 3: Consultar Usuarios
Label(pestana3, text="Consultar Usuarios", fg="black", font=("Arial", 18)).pack()


Button(pestana3, text="Consultar Usuarios", command=consultaUsuarios).pack()

text_box_consulta = Text(pestana3, height=5, width=52)
text_box_consulta.pack()

Ventana.mainloop()
