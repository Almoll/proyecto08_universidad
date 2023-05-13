import os

def listar_equipos(equipos):
    print("Equipos disponibles:")
    for equipo in equipos:
        print("- " + equipo["identificador"])

def seleccionar_equipo(equipos):
    while True:
        listar_equipos(equipos)
        identificador = input("Introduce el identificador del equipo o 'c' para cancelar: ")
        if identificador.lower() == 'c':
            return None
        equipo_encontrado = None
        for equipo in equipos:
            if equipo["identificador"] == identificador:
                equipo_encontrado = equipo
                break
        if equipo_encontrado:
            return equipo_encontrado
        else:
            print("Identificador inválido. Introduce un identificador válido o 'c' para cancelar.")

def cambio_configuracion(equipo):
    print("Cambio de configuración del equipo " + equipo["identificador"])
    for tipo, identificador in equipo["componentes_seleccionados"].items():
        print(f"- {tipo}: {identificador}")
        while True:
            opcion = input("¿Quieres cambiar este componente? (s/n): ")
            if opcion.lower() == "s":
                nuevo_identificador = input("Introduce el nuevo identificador del componente o 'c' para cancelar: ")
                if nuevo_identificador.lower() == 'c':
                    break
                equipo["componentes_seleccionados"][tipo] = nuevo_identificador
                print("Componente actualizado.")
                break
            elif opcion.lower() == "n":
                break
            else:
                print("Opción inválida. Introduce 's' para cambiar el componente o 'n' para no cambiarlo.")

def desensamblar_equipo(equipo, equipos):
    print("Desensamblar equipo " + equipo["identificador"])
    equipos.remove(equipo)
    print("Equipo desensamblado.")

# Cargar los equipos existentes del archivo equipos.txt
equipos = []
with open("equipos.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(",")
        identificador = datos[0]
        componentes_seleccionados = {
            " Fuente": datos[1],
            " PB": datos[2],
            " TG": datos[3],
            " CPU": datos[4],
            " RAM": datos[5],
            " Disco": datos[6]
        }
        equipos.append({
            "identificador": identificador,
            "componentes_seleccionados": componentes_seleccionados
        })

# Preguntar al usuario si quiere buscar un equipo o listar todos
while True:
    opcion = input("Introduce 'b' para buscar un equipo, 'l' para listar todos o 'q' para salir: ")
    if opcion.lower() == "b":
        equipo = seleccionar_equipo(equipos)
        if equipo:
            while True:
                opcion = input("Introduce 'c' para cambio de configuración, 'd' para desensamblar o 'v' para volver: ")
                if opcion.lower() == "c":
                    cambio_configuracion(equipo)
                elif opcion.lower() == "d":
                    desensamblar_equipo(equipo, equipos)
                    break
                elif opcion.lower() == "v":
                    break
                else:
                    print("Opción inválida. Introduce 'c' para cambio de configuración, 'd' para desensamblar o 'v' para volver")
    elif opcion.lower() == "l":
        listar_equipos(equipos)
    elif opcion.lower() == "q":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Introduce 'b' para buscar un equipo, 'l' para listar todos o 'q' para salir.")

# Guardar los equipos actualizados en el archivo equipos.txt
with open("equipos.txt", "w") as f:
    for equipo in equipos:
        identificador = equipo["identificador"]
        componentes_seleccionados = equipo["componentes_seleccionados"]
        linea = f"{identificador},{componentes_seleccionados[' Fuente']},{componentes_seleccionados[' PB']},{componentes_seleccionados[' TG']},{componentes_seleccionados[' CPU']},{componentes_seleccionados[' RAM']},{componentes_seleccionados[' Disco']}\n"
        f.write(linea)

print("Programa finalizado.")
