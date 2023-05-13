import os 

componentes = {
    " Fuente": [],
    " PB": [],
    " TG": [],
    " CPU": [],
    " RAM": [],
    " Disco": []
}
def comprobar_identificador(usuarios):
    with open("equipos.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if datos[0] == usuarios:
                return True
    return False
# Crear una lista vacía para almacenar los equipos
equipos = []
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


while True:
    # Pedimos el identificador al usuario
    usuarios = input("Introduce el identificador del equipo (mínimo 3 caracteres alfanuméricos): ")
    if len(usuarios) < 3 or not usuarios.isalnum():
        print("Identificador inválido. Debe tener al menos 3 caracteres alfanuméricos.")
        continue

    # Comprobar si el identificador ya existe
    if comprobar_identificador(usuarios):
        print("El identificador ya existe. Introduce uno nuevo.")
        continue
    else:
        print("El identificador es válido.")

    # Mostramos los componentes disponibles para cada tipo
    componentes_seleccionados = {}
    for tipo, identificadores in componentes.items():
        print(f"\nSelecciona una opción de {tipo} (o 'c' para cancelar):")
        for i, identificador in enumerate(identificadores):
            print(f"{i + 1}) {identificador}")
        while True:
            opcion_seleccionada = input("Introduce el número de la opción que deseas, o 'c' para cancelar: ")
            if opcion_seleccionada.lower() == 'c':
                print("Creación de equipo cancelada.")
                os.system ("equipos.py")
                break
            elif opcion_seleccionada.isnumeric() and int(opcion_seleccionada) in range(1, len(identificadores) + 1):
                componentes_seleccionados[tipo] = identificadores[int(opcion_seleccionada) - 1]
                break
            else:
                print("Opción inválida.")
        if opcion_seleccionada.lower() == 'c':
            break


    # Añadimos el equipo a la lista de equipos
    equipo = {
        "identificador": usuarios,
    }
    equipos.append((usuarios, componentes_seleccionados))

    # Escribimos el equipo en el archivo equipos.txt
    with open("equipos.txt", "a") as f:
        f.write(f"{usuarios},{componentes_seleccionados[' Fuente']},{componentes_seleccionados[' PB']},{componentes_seleccionados[' TG']},{componentes_seleccionados[' CPU']},{componentes_seleccionados[' RAM']},{componentes_seleccionados[' Disco']}\n")

    # Actualizamos la cantidad de componentes disponibles
    for tipo, identificadores in componentes.items():
        if componentes_seleccionados[tipo] in identificadores:
            identificadores.remove(componentes_seleccionados[tipo])

    # Preguntamos al usuario si quiere introducir otro equipo
    respuesta = input("¿Quieres introducir otro equipo? (s/n): ")
    if respuesta.lower() == "n":
        os.system ("equipos.py")
        break



print("Equipos introducidos:")
for identificador, componentes_seleccionados in equipos:
    print(f"\nEquipo {identificador}:")
    for tipo, identificador in componentes_seleccionados.items():
        print(f"- {tipo}: {identificador}")


