entero = 50

with open ("QAP_sko56_04_n") as files:
#from ("QAP_sko56_04_n") import files
asdsa
# Carga el archivo QAP_aasdsdasdsko56_04_n.txt desde tu computadora local al entorno de Colab
uploaded = files.upload()

# Abre el archivo
with open("S8", 'r') as archivo:
    # Tu código para procesar el archivo


# Lee todas las líneas del archivo
    lineas = archivo.readlines()
# Extrae la cantidad de puestos del primer elemento
cantidad_puestos = int(lineas[0])

# Extrae los tamaños de los puestos de la segunda línea
tamaños_puestos = list(map(int, lineas[1].split(',')))


# Inicializa una matriz para almacenar los datos de clientes
clientes = []
for linea in lineas[2:]:
    valores = linea.split(',')
    fila = list(map(int, valores))
    clientes.append(fila)

# Imprime la cantidad de puestos
print("Cantidad de puestos:", cantidad_puestos)

#Imprime los tamaños de los puestos
print("Tamaños de los puestos:", tamaños_puestos)

# Imprime los datos de clientes
print("Datos de clientes:")
for fila in clientes:
    print(fila)
