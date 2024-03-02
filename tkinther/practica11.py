from tkinter import Tk, Frame

#1.Creamos la ventana
ventana= Tk() #Uso de POO creando un objeto ventana
ventana.title('Ejemplo con tres frames')
ventana.geometry('600x400')

#colocamos las secciones o frames de la ventana
seccion1= Frame(ventana, bg='light green')
seccion1.pack(expand=True, fill='both')
seccion2= Frame(ventana, bg='light blue')
seccion2.pack(expand=True, fill='both')
seccion3= Frame(ventana, bg='light coral')
seccion3.pack(expand=True, fill='both')
#Ejecuta 
ventana.mainloop()