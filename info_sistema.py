import os
while True:
    print("¿Qué quieres ver?\n")
    print("1. Componentes")
    print("2. Equipos")
    print("3. Distribuidores")
    print("0. Cancelar\n")
    
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == "1":
        print("Has seleccionado ver Componentes.")
        # Abrir el archivo y leer su contenido
        with open("componentes.txt", "r") as archivo:
            contenido = archivo.read()
        # Mostrar el contenido del archivo
        print(contenido)
        # Aquí puedes añadir el código para mostrar los componentes
        
    elif opcion == "2":
        while True:
            print("\n¿Qué quieres ver de Equipos?\n")
            print("1. Equipos enteros")
            print("2. Despachar")
            print("3. Entregados")
            print("0. Volver\n")
            
            opcion_equipo = input("Ingrese el número de la opción deseada: ")
            
            if opcion_equipo == "1":
                print("Has seleccionado ver Equipos enteros.")
                # Aquí puedes añadir el código para mostrar los equipos enteros
                # Abrir el archivo y leer su contenido
                with open("equipos.txt", "r") as archivo:
                    contenido = archivo.read()
                # Mostrar el contenido del archivo
                print(contenido)
            elif opcion_equipo == "2":
                print("Has seleccionado ver Despachar.")
                # Aquí puedes añadir el código para mostrar los despachos de equipos
                # Abrir el archivo y leer su contenido
                with open("despachar.txt", "r") as archivo:
                    contenido = archivo.read()
                # Mostrar el contenido del archivo
                print(contenido)
            elif opcion_equipo == "3":
                print("Has seleccionado ver Entregados.")
                # Aquí puedes añadir el código para mostrar los equipos que ya han sido entregados
                
            elif opcion_equipo == "0":
                break # Salir del ciclo y volver al menú principal
            
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
            
    elif opcion == "3":
        print("Has seleccionado ver Distribuidores.")
        # Aquí puedes añadir el código para mostrar los distribuidores
        # Abrir el archivo y leer su contenido
        with open("distribuidores.txt", "r") as archivo:
            contenido = archivo.read()
        # Mostrar el contenido del archivo
        print(contenido)
    elif opcion == "0":
        os.system ("menuprincipal.py")
        break # Salir del ciclo principal y terminar el programa
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
