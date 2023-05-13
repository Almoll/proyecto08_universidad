import os
archivo_componentes = 'componentes.txt'

# Función para mostrar el menú de componentes
def menu_equipos():
    print("Opción 1: Equipos")
    print("Elige una opción: ")
    print("1) Añadir  Equipos")
    print("2) Modificar Equipos")
    print("0) Volver al menú principal")


# Aqui se muestra el menu de componentes y sus funciones
def equipos(opcion):
    if opcion == "1":
        os.system ("equipos2.py")
        # en la primera opcion se añade un equipo a la lista de datos
        pass
    elif opcion == "2":
        os.system ("equipos3.py")
        # enlla segunsda se modifica un equipo de la lista
        pass
    elif opcion == "0":
        os.system ("menuprincipal.py")
        #volver al primer menu
    else:
        print("Opción no disponible.Por favor, eliga una opción del menú.")

menu_equipos()
opcion_equipos = input("Elige una opción: ")
equipos(opcion_equipos)