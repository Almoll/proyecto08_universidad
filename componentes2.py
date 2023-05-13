import os

class Componente:
    def __init__(self, identificador, tipo, peso, coste, cantidad):
        self.identificador = identificador
        self.tipo = tipo
        self.peso = peso
        self.coste = coste
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.identificador}|{self.tipo}|{self.peso}|{self.coste}|{self.cantidad}"

def cargar_componentes():
    componentes = {}
    with open("componentes.txt", "r") as archivo:
        for linea in archivo:
            identificador, tipo, peso, coste, cantidad = linea.strip().split("|")
            componente = Componente(int(identificador), tipo, float(peso), float(coste), int(cantidad))
            componentes[componente.identificador] = componente
    return componentes

def listar_componentes(componentes):
    print("Identificadores de componentes en sistema:")
    for identificador in componentes:
        print(identificador)

def buscar_componente(componentes, identificador):
    if identificador in componentes:
        return componentes[identificador]
    else:
        return None

def escribir_componentes(componentes):
    with open("componentes.txt", "w") as archivo:
        for componente in componentes.values():
            archivo.write(str(componente) + "\n")

def dar_de_baja(componentes, identificador):
    componente = buscar_componente(componentes, identificador)
    if componente:
        del componentes[identificador]
        escribir_componentes(componentes)
        print(f"El componente {identificador} ha sido dado de baja.")
    else:
        print("Identificador inválido.")

def cambiar_stock(componentes, identificador):
    componente = buscar_componente(componentes, identificador)
    if componente:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        componente.cantidad = nueva_cantidad
        escribir_componentes(componentes)
        print(f"El stock del componente {identificador} ha sido actualizado.")
    else:
        print("Identificador inválido.")

def cambiar_informacion(componentes, identificador):
    componente = buscar_componente(componentes, identificador)
    if componente:
        print(f"Información actual del componente {identificador}:")
        print(f"Tipo: {componente.tipo}")
        print(f"Peso: {componente.peso}")
        print(f"Coste: {componente.coste}")
        print(f"Cantidad: {componente.cantidad}")
        opcion = input("¿Qué información desea modificar? (T)ipo, (P)eso, (C)oste, (Q)uantidad: ")
        if opcion == "T":
            nuevo_tipo = input("Ingrese el nuevo tipo: ")
            componente.tipo = nuevo_tipo
            escribir_componentes(componentes)
            print(f"El tipo del componente {identificador} ha sido actualizado.")
        elif opcion == "P":
            nuevo_peso = float(input("Ingrese el nuevo peso: "))
            componente.peso = nuevo_peso
            escribir_componentes(componentes)
            print(f"El peso del componente {identificador} ha sido actualizado.")
        elif opcion == "C":
            nuevo_coste = float(input("Ingrese el nuevo coste: "))
            componente.coste = nuevo_coste
            escribir_componentes(componentes)
            print(f"El coste del componente {identificador} ha sido actualizado.")
        elif opcion == "Q":
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            componente.cantidad = nueva_cantidad
            escribir_componentes(componentes)
            print(f"El stock del componente {identificador} ha sido actualizado.")
        else:
            print("Opción inválida.")
    else:
        print("Identificador inválido.")

def main():
    componentes = cargar_componentes()
    while True:
        opcion = input("Ingrese 'L' para listar componentes , ingrese un identificador para modificar información O ingrese 'V' para volver: ").strip()
        if opcion == "L":
            listar_componentes(componentes)
        elif opcion == "V":
            os.system ("componentes.py")
        else:
            identificador = int(opcion)
            if buscar_componente(componentes, identificador):
                accion = input("¿Qué acción desea realizar? (C)ambio Stock, Cambio (I)nformación, (D)ar de baja: ").strip()
                if accion == "C":
                    cambiar_stock(componentes, identificador)
                elif accion == "I":
                    cambiar_informacion(componentes, identificador)
                elif accion == "D":
                    dar_de_baja(componentes, identificador)
                else:
                    print("Acción inválida.")
            else:
                print("Identificador inválido.")
                
if __name__ == "__main__":
    main()
