import re

# Especifica la ruta al archivo en tu sistema local
archivo_path = "S5.txt"  # Reemplaza con la ruta real del archivo

# Abre el archivo en modo lectura
with open(archivo_path, 'r') as archivo:
    # Lee todas las líneas del archivo
    lineas = archivo.readlines()

# Extrae la cantidad de puestos del primer elemento
cantidad_puestos = int(lineas[0])

# Extrae los tamaños de los puestos de la segunda línea
tamaños_puestos = list(map(int, lineas[1].split(',')))

# Extrae la cantidad de clientes estimados entre pares de puestos en una matriz simétrica
clientes_estimados = []
for linea in lineas[2:]:
    valores = list(map(int, linea.split(',')))
    clientes_estimados.append(valores)

# Imprime la información
print("Cantidad de puestos:", cantidad_puestos)
print("Tamaños de los puestos:", tamaños_puestos)
print("Clientes estimados entre pares de puestos:")
for fila in clientes_estimados:
    print(fila)

