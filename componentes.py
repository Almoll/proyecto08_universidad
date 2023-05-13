import os

# pafa conectar con el txt temporalmente
archivo_componentes = 'componentes.txt'
# Función para mostrar el menú de componentes
def menu_componentes():
    print("Opción 1: Componentes")
    print("Elige una opción: ")
    print("1) Añadir componenetes")
    print("2) Modificar componentes")
    print("0) Volver al menú principal")



# Aqui se muestra el menu de componentes y sus funciones
def componentes(opcion):
    if opcion == "1":
        os.system ("componentes3.py")
        # en la primera opcion te mueve para añadir un componenete
        pass
    elif opcion == "2":
        os.system ("componentes2.py")
        # en ella segunsda se modifica un indicador
        pass
    elif opcion == "0":
        os.system ("menuprincipal.py")
        #volver al primer menu
    else:
        print("Opción no disponible.Por favor, eliga una opción del menú.")

# Mostrar el menú componentes al iniciar el programa
menu_componentes()
opcion_componentes = input("Elige una opción: ")
componentes(opcion_componentes)