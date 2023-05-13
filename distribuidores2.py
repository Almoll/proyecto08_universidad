import os 

def agregar_distribuidor():
    while True:
        # Solicitar al usuario el identificador, validar que tenga al menos tres dígitos
        identificador = input("Introduce el identificador del distribuidor (mínimo 3 dígitos): ")
        if not identificador.isdigit() or len(identificador) < 3:
            print("Por favor, introduce un identificador válido con al menos tres dígitos.")
            continue
        
        # Validar que el identificador no exista en el archivo de texto
        with open("distribuidores.txt", "r") as f:
            lineas = f.readlines()
            for linea in lineas:
                if linea.startswith(identificador):
                    print("Ya existe un distribuidor con ese identificador.")
                    identificador = None
                    break

        if identificador is None:
            continue
        
        respuesta = input("Introduce el nombre del distribuidor: ")
        tiempo_entrega = input("Introduce el tiempo de entrega en días: ")
        direccion = input("Introduce la dirección del distribuidor (máximo 100 caracteres): ")

        # Validar que los campos no estén vacíos y que el tiempo de entrega sea un número entero
        if not respuesta or not tiempo_entrega.isdigit() or not direccion:
            print("Por favor, introduce todos los campos correctamente.")
            continue

        # Guardar los datos en un archivo de texto
        with open("distribuidores.txt", "a") as f:
            f.write(f"{identificador},{respuesta},{tiempo_entrega},{direccion}\n")

        respuesta = input("¿Quieres agregar otro distribuidor? (s/n): ")
        if respuesta.lower() != "s":
            os.system ("distribuidores.py")
            break
if __name__ == "__main__":
    agregar_distribuidor()