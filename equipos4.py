import os

componentes = {
    " Fuente": [],
    " PB": [],
    " TG": [],
    " CPU": [],
    " RAM": [],
    " Disco": []
}

def cargar_componentes():
    with open("componentes.txt", "r") as archivo:
        lineas = archivo.read().splitlines()

    for linea in lineas:
        datos = linea.split("|")
        if len(datos) == 5:
            identificador, tipo, peso , coste, stock = datos
            if tipo in componentes:
                componentes[tipo].append({
                    "tipo": tipo,
                    "identificador": identificador,
                    "peso": peso,
                    "coste": coste,
                    "stock": int(stock)
                })

def comprobar_identificador(usuarios):
    with open("equipos.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if datos[0] == usuarios:
                return True
    return False
# Abrir el archivo equipos.txt y leer su contenido
with open("equipos.txt", "r") as f:
    lineas = f.readlines()

# Buscar el equipo a editar en el archivo
indice_editar = None
for i, linea in enumerate(lineas):
    datos = linea.strip().split(",")
    if datos[0] == identificador_editar:
        indice_editar = i
        componentes_editar = {
            " Fuente": datos[1],
            " PB": datos[2],
            " TG": datos[3],
            " CPU": datos[4],
            " RAM": datos[5],
            " Disco": datos[6]
        }
        break

if indice_editar is None:
    print(f"No se encontró un equipo con identificador {identificador_editar}.")
else:
    # Pedir al usuario el tipo de componente que desea cambiar
    while True:
        tipo_componente = input("Introduce el tipo de componente que deseas cambiar (o 'c' para cancelar): ")
        if tipo_componente.lower() == 'c':
            print("Edición de equipo cancelada.")
            break
        elif tipo_componente not in componentes_editar:
            print(f"No se encontró ningún componente de tipo {tipo_componente} en el equipo.")
        else:
            # Mostrar los componentes disponibles del mismo tipo
            componentes_tipo = componentes[tipo_componente]
            print(f"Componentes disponibles de tipo {tipo_componente}:")
            for i, comp in enumerate(componentes_tipo):
                print(f"{i+1}) {comp['identificador']}")

            # Pedir al usuario el componente nuevo
            while True:
                num_componente = input("Introduce el número del componente que deseas (o 'c' para cancelar): ")
                if num_componente.lower() == 'c':
                    print("Edición de equipo cancelada.")
                    break
                elif not num_componente.isnumeric() or int(num_componente) not in range(1, len(componentes_tipo)+1):
                    print("Opción inválida.")
                else:
                    # Actualizar el componente en el diccionario componentes_editar
                    componente_nuevo = componentes_tipo[int(num_componente)-1]
                    componentes_editar[tipo_componente] = componente_nuevo["identificador"]
                    print(f"Componente {componente_nuevo['identificador']} de tipo {tipo_componente} seleccionado.")
                    break

            # Escribir la información actualizada del equipo en el archivo
            lineas[indice_editar] = f"{identificador_editar},{componentes_editar[' Fuente']},{componentes_editar[' PB']},{componentes_editar[' TG']},{componentes_editar[' CPU']},{componentes_editar[' RAM']},{componentes_editar[' Disco']}\n"
            with open("equipos.txt", "w") as f:
                f.writelines(lineas)
            print("Equipo actualizado.")
        break

def seleccionar_componente(tipo):
    identificadores = componentes[tipo]
    print(f"Componentes disponibles de tipo {tipo}:")
    for i, identificador in enumerate(identificadores):
        print(f"{i + 1}) {identificador['identificador']}")

    while True:
        opcion_seleccionada = input("Introduce el número de la opción que deseas, o 'c' para cancelar: ")
        if opcion_seleccionada.lower() == 'c':
            return None
        elif opcion_seleccionada.isnumeric() and int(opcion_seleccionada) in range(1, len(identificadores) + 1):
            return identificadores[int(opcion_seleccionada) - 1]
        else:
            print("Opción inválida.")

def editar_equipo():
    # Pedir el identificador del equipo a editar
    identificador = input("Introduce el identificador del equipo a editar: ")

    # Comprobar si el identificador existe
    with open("equipos.txt", "r") as f:
        equipo_encontrado = False
        for linea in f:
            datos = linea.strip().split(",")
            if datos[0] == identificador:
                equipo_encontrado = True
                componentes_actuales = {
                    " Fuente": datos[1],
                    " PB": datos[2],
                    " TG": datos[3],
                    " CPU": datos[4],
                    " RAM": datos[5],
                    " Disco": datos[6]
                }
                break

        if not equipo_encontrado:
            print("El identificador no existe.")
            return

    # Mostrar los componentes actuales del equipo
    print("Componentes actuales:")
    for tipo, identificador in componentes_actuales.items():
        print(f"- {tipo}: {identificador}")

    # Pedir al usuario qué componente desea cambiar
    while True:
        tipo_a_cambiar = input("Introduce el tipo de componente que deseas cambiar (o 'c' para cancelar): ")
        if tipo_a_cambiar.lower() == 'c':
            print("Edición de equipo cancelada.")
            return
        elif tipo_a_cambiar not in componentes_actuales:
            print("Tipo de componente inválido.")
        else:
            break

    # Mostrar los componentes disponibles para el tipo seleccionado
    componentes_disponibles = []
    with open("componentes.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split("|")
            if len(datos) == 5 and datos[1] == tipo_a_cambiar:
                identificador, tipo, peso, coste, stock = datos
                componentes_disponibles.append({
                    "tipo": tipo,
                    "identificador": identificador,
                    "peso": peso,
                    "coste": coste,
                    "stock": int(stock)
                })

    print(f"\nComponentes disponibles para {tipo_a_cambiar}:")
    for i, componente in enumerate(componentes_disponibles):
        print(f"{i + 1}) {componente['identificador']}")

    # Pedir al usuario el nuevo componente
    while True:
        opcion_seleccionada = input("Introduce el número de la opción que deseas, o 'c' para cancelar: ")
        if opcion_seleccionada.lower() == 'c':
            print("Edición de equipo cancelada.")
            return
        elif opcion_seleccionada.isnumeric() and int(opcion_seleccionada) in range(1, len(componentes_disponibles) + 1):
            nuevo_componente = componentes_disponibles[int(opcion_seleccionada) - 1]
            break
        else:
            print("Opción inválida.")

    # Actualizar el componente del equipo
    componentes_actuales[tipo_a_cambiar] = nuevo_componente['identificador']

    # Escribir el equipo actualizado en el archivo equipos.txt
    with open("equipos.txt", "r") as f:
        lineas = f.readlines()
    with open("equipos.txt", "w") as f:
        for linea in lineas:
            datos = linea.strip()

if __name__ == '__main__':
    editar_equipo()
