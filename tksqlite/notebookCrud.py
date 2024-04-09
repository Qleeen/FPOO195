from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *
from GeneradorPDF import *
import os


# Llamamos a nuestra clase Controlador
objControlador = Controlador()
objPDF = GeneradorPDF()

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

def ejecutaPDF():
    if varTitulo=="":
        messagebox.showwarning("Escribe un nombre al PDF")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varTitulo.get() + ".pdf")
        rutaPDF = "/Users/baru/Documents/5to cuatri/POO/Github/FPOO195/tksqlite/GeneradorPDF.py" +varTitulo.get() + ".pdf"
        messagebox.showinfo("Archivo creado", "PDF disponible en carpeta")
        os.system(f"start{rutaPDF}")
    
    
#1 crear la ventana
Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("800x500")

#2. preparar el notebook para pestañas
panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

#3. Pestañas que ocuparemos para el panel
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)
pestana6 = ttk.Frame(panel)

#4 Agregaremos las pesatañas que queremos crear al panel
panel.add(pestana1, text="Crear Usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Editar Usuario")
panel.add(pestana5, text="Eliminar Usuario")
panel.add(pestana6, text="Reportes en PDF")

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

#Pestaña 8: Exportar PDF
Label(pestana6, text="Reportes en PDF", fg="black", font=("Modern", 18)).pack()

varTitulo = tk.StringVar()
Label(pestana6, text="Escribe el titulo de tu archivo").pack()
Entry(pestana6, textvariable=varTitulo).pack()
Button(pestana6, text="Crear PDF", command=ejecutaPDF).pack()

Ventana.mainloop()

