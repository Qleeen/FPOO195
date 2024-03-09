from tkinter import Tk, Frame, Button, StringVar, Label, Entry, messagebox

#1.Creamos la ventana
ventana= Tk() 
ventana.title('Login')
ventana.geometry('600x400')




contrasena = StringVar()




Label(ventana, text="Longitud").pack()
Entry(ventana, textvariable=contrasena, show='*').pack()


seccion1= Frame(ventana, bg='white')
seccion1.pack(expand=True, fill='both')

def mostrarMensajes():
    print(messagebox.askquestion(message= '¿Quieres Mayúsculas?', title='Pregunta'))
    print(messagebox.askquestion(message= '¿Quieres Caracteres?', title='Pregunta'))
    




botonValidar= Button(seccion1, text='Generar', fg='black', command=mostrarMensajes)
botonValidar.place(x=100, y=60, width=150, height=30)
botonValidar.pack()
    
    
    

#Ejecuta 
ventana.mainloop()