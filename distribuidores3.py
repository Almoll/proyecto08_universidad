import os 
# función para mostrar los identificadores de los distribuidores
def mostrar_identificadores():
    with open("distribuidores.txt", "r") as f:
        print("Lista de distribuidores:")
        for linea in f:
            id, nombre, tiempo_entrega, direccion = linea.strip().split(',')
            print(f"- {id}")
        print()

# función para cambiar la información de un distribuidor
def cambiar_informacion(id):
    encontrado = False
    with open("distribuidores.txt", "r") as f:
        lineas = f.readlines()
    with open("distribuidores.txt", "w") as f:
        for linea in lineas:
            campos = linea.strip().split(',')
            if campos[0] == id:
                nombre = input("Ingrese el nuevo nombre del distribuidor (o 'cancelar' para salir): ")
                if nombre.lower() == 'cancelar':
                    os.system ("distribuidores.py")
                    return
                tiempo_entrega = input("Ingrese el nuevo tiempo de entrega (en días) (o 'cancelar' para salir): ")
                if tiempo_entrega.lower() == 'cancelar':
                    os.system ("distribuidores.py")
                    return
                direccion = input("Ingrese la nueva dirección del distribuidor (o 'cancelar' para salir): ")
                if direccion.lower() == 'cancelar':
                    os.system ("distribuidores.py")
                    return
                nueva_linea = f"{id},{nombre},{tiempo_entrega},{direccion}\n"
                f.write(nueva_linea)
                encontrado = True
            else:
                f.write(linea)
    if encontrado:
        print("La información del distribuidor ha sido actualizada.")
    else:
        print("El identificador no existe.")

# función para dar de baja a un distribuidor
def dar_de_baja(id):
    encontrado = False
    with open("distribuidores.txt", "r") as f:
        lineas = f.readlines()
    with open("distribuidores.txt", "w") as f:
        for linea in lineas:
            campos = linea.strip().split(',')
            if campos[0] == id:
                confirmacion = input(f"¿Está seguro que desea dar de baja al distribuidor {campos[1]}? (S/N): ")
                if confirmacion.lower() == 's':
                    encontrado = True
                else:
                    f.write(linea)
            else:
                f.write(linea)
    if encontrado:
        print("El distribuidor ha sido dado de baja.")
    else:
        print("El identificador no existe.")

# programa principal
while True:
    opcion = input("Ingrese 'L' para listar los distribuidores o el identificador de un distribuidor (o 'cancelar' para salir): ")
    if opcion.lower() == 'cancelar':
        os.system ("distribuidores.py")
        break
    elif opcion == 'L':
        mostrar_identificadores()
        id = input("Ingrese el identificador del distribuidor (o 'cancelar' para salir): ")
        if id.lower() == 'cancelar':
            os.system ("distribuidores.py")
            break
    else:
        id = opcion
    accion = input("Ingrese 'C' para cambiar la información o 'B' para dar de baja al distribuidor (o 'cancelar' para salir): ")
    if accion.lower() == 'cancelar':
        os.system ("distribuidores.py")
        break
    elif accion == 'C':
        cambiar_informacion(id)
    elif accion == 'B':
        dar_de_baja(id)
    else:
        print("Opción inválida.")
