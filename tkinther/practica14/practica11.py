from tkinter import Tk, Frame, Button, messagebox

#metodos para mensajes
def mostrarMensajes():
    print(messagebox.showinfo('showinfo', 'Information'))
    print(messagebox.showerror('showerror', 'Error'))
    print(messagebox.showwarning('showwarning', 'Warning'))
    print(messagebox.askquestion(message= '¿Es usted?', title='Pregunta'))
    
#
def addbtn():
    botonVerde.config(text='+')
    botonrosa= Button(seccion3, text='Nuevo', fg= 'green', background='#30B316')
    botonrosa.configure(height=3, width=5)
    botonrosa.pack()



#1.Creamos la ventana
ventana= Tk() #Uso de POO creando un objeto ventana
ventana.title('Ejemplo con tres frames')
ventana.geometry('600x400')

#colocamos las secciones o frames de la ventana
seccion1= Frame(ventana, bg='black')
seccion1.pack(expand=True, fill='both')
seccion2= Frame(ventana, bg='gray')
seccion2.pack(expand=True, fill='both')
seccion3= Frame(ventana, bg='white')
seccion3.pack(expand=True, fill='both')


#3. Posicionar botones

#place
botonAzul= Button(seccion1, text='Azul', fg='blue')
botonAzul.place(x=100, y=60, width=100, height=30)

#grid
botonNegro= Button(seccion2, text='Negro', fg= 'brown', bg='#090909')
botonNegro.configure(height= 2, width= 10)
#posicionar
botonNegro.grid(row=0, column=1)

botonAmarillo= Button(seccion2, text='Amarillo', fg= 'yellow', bg='#fbff00', command=mostrarMensajes)
botonAmarillo.configure(height=2, width=10)
botonAmarillo.grid(row=1, column=2)

#pack
botonVerde= Button(seccion3, text='Verde', fg= 'green', bg='#30B316', command=addbtn)
botonVerde.configure(height=2, width=10)
botonVerde.pack()



#Ejecuta 
ventana.mainloop()