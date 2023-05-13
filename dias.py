import os


# Pedir al usuario que ingrese el identificador del archivo
archivo = input("Ingrese el identificador del archivo: ")

# Preguntar al usuario cuántos días han pasado desde una fecha específica
dias_pasados = int(input("¿Cuántos días han pasado desde la fecha específica? "))

# Leer el dato específico del archivo
with open('despachar.txt', 'r') as f:
    dato = int(f.readline().strip())

# Restar los días ingresados al dato específico
resultado = dato - dias_pasados

# Si el resultado de la resta es menor o igual a 0, mover el archivo a un nuevo archivo
if resultado <= 0:
    # Crear el nombre del nuevo archivo
    nuevo_archivo = f"{archivo}_movido.txt"
    
    # Mover el archivo a un nuevo archivo
    os.rename(archivo, nuevo_archivo)
    print(f"El archivo {archivo} se ha movido a {nuevo_archivo}")
else:
    # Escribir el resultado de la resta en el archivo
    with open(archivo, 'a') as f:
        f.write(str(resultado))
        print(f"El nuevo valor del dato es: {resultado}")
