from Persona import *
usuarios = {}

def mostrar_menu():
    print("Menú funcional:")
    print("1. Agregar usuario")
    print("2. Consultar usuario")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("0. Salir")

def mostrar_menu_modificar():
    print("¿Qué dato desea modificar?")
    print("1. Nombre")
    print("2. Apellido paterno")
    print("3. Apellido materno")
    print("4. Correo")
    print("5. Contraseña")

def main():
    opcion = None
    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            id = input("Ingrese ID: ")
            nom = input("Ingrese nombre: ")
            pat = input("Ingrese apellido paterno: ")
            mat = input("Ingrese apellido materno: ")
            corr = input("Ingrese correo: ")
            cont = input("Ingrese contraseña: ")
            usuarios[id] = Persona(id, nom, pat, mat, corr, cont)
            print('Se ha agregado un nuevo usuario')
        elif opcion == 2:
            id = input("Ingrese ID del usuario a consultar: ")
            if id in usuarios:
                usuarios[id].consultar()
            else:
                print("Usuario no encontrado.")
        elif opcion == 3:
            id = input("Ingrese ID del usuario a modificar: ")
            if id in usuarios:
                mostrar_menu_modificar()
                opcion_modificar = int(input("Ingrese una opción: "))
                if opcion_modificar == 1:
                    nuevo_nombre = input("Ingrese nuevo nombre: ")
                    usuarios[id].setNombre(nuevo_nombre)
                elif opcion_modificar == 2:
                    nuevo_apellidoP = input("Ingrese nuevo apellido paterno: ")
                    usuarios[id].setApellidoP(nuevo_apellidoP)
                elif opcion_modificar == 3:
                    nuevo_apellidoM = input("Ingrese nuevo apellido materno: ")
                    usuarios[id].setApellidoM(nuevo_apellidoM)
                elif opcion_modificar == 4:
                    nuevo_correo = input("Ingrese nuevo correo: ")
                    usuarios[id].setCorreo(nuevo_correo)
                elif opcion_modificar == 5:
                    nueva_contrasena = input("Ingrese nueva contraseña: ")
                    usuarios[id].setContrasena(nueva_contrasena)
                print('Se ha modificado el usuario')
            else:
                print("Usuario no encontrado.")
        elif opcion == 4:
            id = input("Ingrese ID del usuario a eliminar: ")
            if id in usuarios:
                del usuarios[id]
                print('Se ha eliminado el usuario')
            else:
                print("Usuario no encontrado.")
        elif opcion == 0:
            print("Bye me fui")
        else:
            print("intente de nuevo.")

if __name__ == "__main__":
    main()