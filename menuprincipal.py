import os

# pafa conectar con el txt temporalmente
archivo_componentes = 'componentes.txt'

# esta es una funcion que muestra las opciones del primer menu
def menu_principal():
    print("¡Bienvenido al programa!")
    print("Elige una opcion:")
    print("1) Componentes")
    print("2) Equipos")
    print("3) Distribuidores")
    print("4) Despachar")
    print("5) Días")
    print("6) Info sistema")
    print("7) Ficheros")
    print("0) Salir")


# Función para manejar la elección del usuario
def manejar_opcion(opcion):
    if opcion == "1":
        os.system ("componentes.py") 
        #te mueve a menu componentes
    elif opcion == "2":
        os.system ("equipos.py")
        # te mueve a menu equipos
        pass
    elif opcion == "3":
        os.system ("distribuidores.py")
        # te mueve a distribuidores
        pass
    elif opcion == "4":
        os.system ("despachar.py")
        # te mueve a despachar
        pass
    elif opcion == "5":
        #os.system ("dias.py")
        #  te mueve a dias
        pass
    elif opcion == "6":
        os.system ("info_sistema.py")
        # te mueve a info_sistema
        pass
    elif opcion == "7":
        # opción 7
        pass
    elif opcion == "0":
        # Salir del programa
        print("¡Hasta luego!")
        exit()
    else:
        print("Opción no disponible.Por favor, eliga una opción del menú.")



# Mostrar el menú principal al iniciar el programa
menu_principal()
opcion_principal = input("Elige una opción: ")
manejar_opcion(opcion_principal)

