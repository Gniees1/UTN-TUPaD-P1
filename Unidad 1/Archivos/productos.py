
print("Ejercicio 2:  \n ")

def mostrar_productos(nombre_archivo="productos.txt"):
    #El encoding sirve para que el los datos del archivo
    #se lean correctamente de poseer caracteres especiales o un alfabeto distinto
    #readlines funciona para leer los datos por lineas  
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.readlines()
    

    for linea in contenido:
        linea = linea.strip()
        partes = linea.split(",")
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")


mostrar_productos()


print("Ejercicio 3:  \n ")

print("Agregue un nuevo producto")

NuevoProd = input(" Ingrese nombre del nuevo producto: ").capitalize()
NuevoPrec = float(input(" Ingrese precio del nuevo producto: "))
NuevaCant = int(input(" Ingrese la cantidad del nuevo productos: "))

with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"\n{NuevoProd},{NuevoPrec},{NuevaCant}\n")

mostrar_productos()



print("Ejercicio 4:  \n ")

productos = []

with open("productos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.readlines()

for linea in contenido:
    linea = linea.strip()
    partes = linea.split(",")
    producto = {
        "nombre": partes[0],
        "precio": float(partes[1]),
        "cantidad": int(partes[2])
    }
    productos.append(producto)
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")




print("Ejercicio 5:  \n ")


consulta = input(" Ingrese el nombre del producto que desea buscar ").capitalize()
encontrado = False
for p in productos:
    if p["nombre"] == consulta:
        encontrado = True
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

if encontrado == False:
    print("producto no encontrado")


print("Ejercicio 6:  \n ")

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("Los productos ya estan actualizados")
