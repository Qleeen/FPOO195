import tkinter as tk

def verificar_acceso():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Lógica de verificación de acceso (puedes personalizar esto según tus necesidades)
    if usuario == "usuario" and contrasena == "contrasena":
        label_resultado.config(text="Acceso concedido")
    else:
        label_resultado.config(text="Acceso denegado")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de Acceso")

# Crear y colocar widgets en la ventana
tk.Label(ventana, text="Usuario:").pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña:").pack(pady=5)
entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.pack(pady=5)

boton_verificar = tk.Button(ventana, text="Verificar Acceso", command=verificar_acceso)
boton_verificar.pack(pady=10)

label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=5)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
 




