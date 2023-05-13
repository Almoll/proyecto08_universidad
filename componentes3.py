# Definir una lista vacía para almacenar los componentes
import os
componentes = []

# Función para comprobar si el identificador ya existe en la lista de componentes
def comprobar_identificador(identificador):
    for componente in componentes:
        if componente["identificador"] == identificador:
            return True
    return False
def comprobar_identificador(identificador):
    with open("componentes.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split("|")
            if datos[0] == identificador:
                return True
    return False
# Función para solicitar los datos del componente al usuario
def agregar_componente():
    while True:
        identificador = input("Introduce el identificador del componente (mínimo 3 caracteres): ")
        if len(identificador) < 3:
            print("El identificador debe tener al menos 3 caracteres.")
            continue
        if comprobar_identificador(identificador):
            print("El identificador ya existe.")
            continue
        break
    
    while True:
        tipo = input("Introduce el tipo del componente (Fuente, PB, TG, CPU, RAM, Disco): ")
        if tipo not in ["Fuente", "PB", "TG", "CPU", "RAM", "Disco"]:
            print("Tipo de componente inválido.")
            continue
        break
    
    while True:
        peso = input("Introduce el peso en gramos del componente: ")
        if not peso.isdigit() or int(peso) <= 0:
            print("Peso inválido. Debe ser un entero mayor que cero.")
            continue
        break
    
    while True:
        coste = input("Introduce el coste en euros del componente: ")
        try:
            coste = float(coste)
            if coste <= 0:
                raise ValueError
        except ValueError:
            print("Coste inválido. Debe ser un número real mayor que cero.")
            continue
        break
    
    while True:
        cantidad = input("Introduce la cantidad de componentes: ")
        if not cantidad.isdigit() or int(cantidad) <= 0:
            print("Cantidad inválida. Debe ser un entero mayor que cero.")
            continue
        break
    
    componente = {
        "identificador": identificador,
        "tipo": tipo,
        "peso": float(peso),
        "coste": float(coste),
        "cantidad": int(cantidad)
    }
    componentes.append(componente)
    
    while True:
        otro = input("¿Quieres introducir otro componente? (S/N): ")
        if otro.upper() == "S":
            agregar_componente()
        elif otro.upper() == "N":
            guardar_componentes(componentes)
            return
        else:
            print("Opción inválida.")
            continue

# Función para guardar los componentes en un archivo de texto
def guardar_componentes(componentes):
    with open("componentes.txt", "a") as f:
        for componente in componentes:
            f.write(f"{componente['identificador']}| {componente['tipo']}| {componente['peso']}| {componente['coste']}| {componente['cantidad']}\n")
    print("Componentes guardados en el archivo 'componentes.txt'.")
    print(componentes)
    os.system ("componentes.py")

# Ejecutar el programa
agregar_componente()
