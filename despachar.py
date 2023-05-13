import os
# Leer los datos de los equipos desde el archivo equipos.txt
with open('equipos.txt', 'r') as f:
    equipos_dict = {}
    for line in f:
        line = line.strip().split(',')
        key = int(line[0])
        values = []
        for item in line[1:]:
            item = item.strip('{}').split(':')
            values.append({item[0].strip():item[1].strip()})
        equipos_dict[key] = values

# Leer los datos de los distribuidores desde el archivo distribuidores.txt
with open('distribuidores.txt', 'r') as f:
    distribuidores_dict = {}
    for line in f:
        line = line.strip().split(',')
        distribuidor = {
            'id': line[0],
            'nombre': line[1],
            'diasentrega': line[2],
            'direccion': line[3]
        }
        distribuidores_dict[distribuidor['id']] = distribuidor

# Solicitar al usuario un identificador numérico de al menos 3 dígitos
while True:
    identificador = input("Ingrese un identificador numérico de al menos 3 dígitos: ")
    if len(identificador) < 3 or not identificador.isdigit():
        print("El identificador debe tener al menos 3 dígitos numéricos. Intente nuevamente.")
    elif any(identificador in line for line in open('despachar.txt')):
        print("El identificador ya existe en el archivo. Intente nuevamente.")
    else:
        break

# Mostrar al usuario una lista de los equipos disponibles para seleccionar
print("Equipos disponibles:")
for equipo in equipos_dict:
    print(equipo)

# Solicitar al usuario que seleccione un equipo de la lista
while True:
    id_equipo_seleccionado = input("Seleccione un equipo por su identificador: ")
    equipo_valido = False
    for equipo in equipos_dict:
        if equipo == int(id_equipo_seleccionado):
            equipo_valido = True
            break
    if not equipo_valido:
        print("El identificador de equipo no existe. Intente nuevamente.")
    else:
        break

# Mostrar al usuario una lista de los distribuidores disponibles para seleccionar
print("Distribuidores disponibles:")
for id_distribuidor, distribuidor in distribuidores_dict.items():
    print(f"{id_distribuidor}: {distribuidor['nombre']}")

# Solicitar al usuario que seleccione un distribuidor de la lista
while True:
    id_distribuidor_seleccionado = input("Seleccione un distribuidor por su identificador: ")
    if id_distribuidor_seleccionado not in distribuidores_dict:
        print("El identificador de distribuidor no existe. Intente nuevamente.")
    else:
        break

# Crear un nuevo archivo de texto llamado "despachar.txt"
with open('despachar.txt', 'a') as f:
    # Obtener los datos completos del equipo seleccionado
    equipo_seleccionado = equipos_dict[int(id_equipo_seleccionado)]

    # Obtener los datos completos del distribuidor seleccionado
    distribuidor_seleccionado = distribuidores_dict[id_distribuidor_seleccionado]

    # Escribir en el archivo los datos completos del identificador, equipo y distribuidor seleccionados por el usuario
    f.write(f"{identificador}, ")
    f.write(f"id_equipo: {id_equipo_seleccionado}:[ ")
    f.write(f"{identificador},")
    for dato_equipo in equipo_seleccionado:
        for key, value in dato_equipo.items():
            f.write(f"{key}: {value}, ")
    f.write(f"], id_distribuidor: {id_distribuidor_seleccionado}:[")
    f.write(f"{distribuidor_seleccionado['nombre']}, {distribuidor_seleccionado['diasentrega']}, {distribuidor_seleccionado['direccion']}]\n")
os.system ("menuprincipal.py")