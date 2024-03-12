import tkinter as tk
from tkinter import simpledialog

class AlmacenApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Administrador de Solicitudes de Almacén")

        self.solicitudes = {}

        self.etiqueta_producto = tk.Label(master, text="Producto:")
        self.etiqueta_producto.pack(pady=5)

        self.entry_producto = tk.Entry(master)
        self.entry_producto.pack(pady=5)

        self.etiqueta_cantidad = tk.Label(master, text="Cantidad:")
        self.etiqueta_cantidad.pack(pady=5)

        self.entry_cantidad = tk.Entry(master)
        self.entry_cantidad.pack(pady=5)

        self.boton_solicitar = tk.Button(master, text="Solicitar Producto", command=self.solicitar_producto)
        self.boton_solicitar.pack(pady=5)

        self.boton_procesar = tk.Button(master, text="Procesar Solicitudes", command=self.procesar_solicitudes)
        self.boton_procesar.pack(pady=5)

        self.boton_mostrar = tk.Button(master, text="Mostrar Solicitudes", command=self.mostrar_solicitudes)
        self.boton_mostrar.pack(pady=10)

        self.resultado = tk.Label(master, text="")
        self.resultado.pack(pady=5)

    def solicitar_producto(self):
        producto = self.entry_producto.get()
        cantidad = int(self.entry_cantidad.get())

        if producto in self.solicitudes:
            self.solicitudes[producto] += cantidad
        else:
            self.solicitudes[producto] = cantidad

        self.mostrar_resultado(f"Solicitud registrada: {cantidad} unidades de {producto}")

    def procesar_solicitudes(self):
        mensaje = "Solicitudes Procesadas:\n"
        for producto, cantidad in self.solicitudes.items():
            mensaje += f"{cantidad} unidades de {producto}\n"
        self.solicitudes = {}
        self.mostrar_resultado(mensaje)

    def mostrar_solicitudes(self):
        solicitudes_str = "\n".join([f"{producto}: {cantidad}" for producto, cantidad in self.solicitudes.items()])
        self.mostrar_resultado(f"Solicitudes Pendientes:\n{solicitudes_str}")

    def mostrar_resultado(self, mensaje):
        self.resultado.config(text=mensaje)


if __name__ == "_main_":
    root = tk.Tk()
    app = AlmacenApp(root)
    root.mainloop()
