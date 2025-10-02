Titulos = []
ejemplares = []

try:
    titulo = input("ingrese el titulo a agregar: ").strip()
    if titulo == "":
        raise ValueError("El título no puede estar vacío")
    ejemplar = int(input("ingrese la cantidad de ejemplares del mismo: "))
    Titulos.append(titulo)
    ejemplares.append(ejemplar)
except ValueError:
    print("datos ingresados de manera erronea")

print(Titulos,ejemplares)