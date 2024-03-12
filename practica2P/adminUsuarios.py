import tkinter as tk
from tkinter import simpledialog

def agregar_usuario():
    nuevo_usuario = entry_usuario.get()
    lista_usuarios.insert(tk.END, nuevo_usuario)
    entry_usuario.delete(0, tk.END)  # Limpiar el campo de entrada después de agregar usuario

def editar_usuario():
    seleccionado = lista_usuarios.curselection()
    if seleccionado:
        indice = seleccionado[0]
        usuario_actual = lista_usuarios.get(indice)
        nuevo_nombre = simpledialog.askstring("Editar Usuario", f"Editar usuario '{usuario_actual}':")
        if nuevo_nombre:
            lista_usuarios.delete(indice)
            lista_usuarios.insert(indice, nuevo_nombre)

def borrar_usuario():
    seleccionado = lista_usuarios.curselection()
    if seleccionado:
        lista_usuarios.delete(seleccionado)

def mostrar_usuarios():
    usuarios = lista_usuarios.get(0, tk.END)
    resultado.config(text=f"Usuarios: {', '.join(usuarios)}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Administrador de Usuarios")

# Crear y colocar widgets en la ventana
tk.Label(ventana, text="Nuevo Usuario:").pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar Usuario", command=agregar_usuario)
boton_agregar.pack(pady=5)

boton_editar = tk.Button(ventana, text="Editar Usuario", command=editar_usuario)
boton_editar.pack(pady=5)

boton_borrar = tk.Button(ventana, text="Borrar Usuario", command=borrar_usuario)
boton_borrar.pack(pady=5)

boton_mostrar = tk.Button(ventana, text="Mostrar Usuarios", command=mostrar_usuarios)
boton_mostrar.pack(pady=10)

lista_usuarios = tk.Listbox(ventana)
lista_usuarios.pack(pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack(pady=5)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
