# Se relleno la variable titulos con dos libros de ejemplo.
titulos = ["Aladdin","La Sirenita"]
ejemplares = [7,5]
menu= ["1. Ingresar Titulos ",
       "2. Ingresar ejemplares ", 
       "3. Mostrar Catalogo ",
       "4. Consultar Disponibilidad ",
       "5. Listar agotados",
       "6. Agregar Titulo ",
       "7. Actualizar ejemplares (prestamo/devolucion) ",
       "8. Salir. "]

# la variable pos se utiliza para que las listas titulos y ejemplares funcionen en paralelo
pos = 0
# La variable agot se utiliza para indicar que cuando se sabe hay libros agotados se muestre de manera ordenada el print
agot = 0
stock = 0
# La variable cont se utiliza como indicador para saber si existen libros agotados
cont = 0
# La variable salida se usa para romper el salir del loop del while cuando el usuario elija la opcion 8
salida = False
# Se utiliza la variable exist para validar si un libro esta dentro del catalogo
exist = False 
print("Bienvenido al menu de la biblioteca, Este es nuestro menu de opciones:  ")

for i in menu:
    print(i)
while(salida != True):
    opcion = int(input("Seleccione una opcion del menu: "))
    match opcion:
        case 1:
            titulo= input("Ingrese el nombre del titulo a agregar ").strip()
            if titulo in titulos:
                print("Ese titulo ya forma parte del catalogo ")
            
            else:
                titulos.append(titulo)
                ejemplar = input("ingrese la cantidad de copias del titulo agregado ")
                if ejemplar.isdigit():
                    ejemplar = int(ejemplar)
                    ejemplares.append(ejemplar)
                else:
                    print("Debe ingresar un valor valido")
           
        case 2:
            titulo= input("Ingrese el titulo al que desea agregar copias ").strip()
            
            for i in titulos:
                if titulo == i:
                    exist = True
                    pos = titulos.index(i)
                    ejemplar = input("Ingrese la cantidad de copias que desea agregar: ")
                    if ejemplar.isdigit():
                        ejemplar = int(ejemplar)
                        ejemplares[pos] += ejemplar
                    else:
                        print("Valor Invalido")
            if exist == False:
                print(" El titulo intgresado no pertenece al catalogo ")
            else:
                exist = False
        case 3:
            for i, valor in enumerate(titulos):
                print(valor,ejemplares[i])
            
        case 4:
            titulo = input("Ingrese el titulo del que desea saber el stock ").strip()
            for i in titulos:
                if titulo == i:
                    pos = titulos.index(i)
                    stock = ejemplares[pos]
            if stock == 0:
                print("No quedan ejemplares de ese titulo ")
            else:
                print(f"La cantidad de ejemplares del titulo {titulo} es : {stock}")
            
        case 5: 
            
            for i, cantidad in enumerate(ejemplares):
                if cantidad == 0:
                    if agot == 0:
                        print(" Los titulos agotados son: ")
                        agot+=1
                    titulo = titulos[i]
                    cont +=1
                    print(titulo)
            if cont == 0:
                print("No hay titulos agotados")
            
        case 6:
            titulo = input("Ingrese el nuevo titulo que desea agregar")
            ejemplar = int(input("ingrese la cantidad de ejemplares del mismo"))

            if titulo not in titulos:
                titulos.append(titulo)
                ejemplares.append(ejemplar)
            else:
                print("El titulo ya existe en la coleccion")
            
        case 7:
            act = input("Ingrese D si desea devolver un ejemplar y P si desea retirar ").upper()
            if act not in ("D","P"):
                print("valor incorrecto")
            if act == "D":
                titulo = input("ingrese el nombre del titulo que desea devolver ").strip()
                if titulo in titulos:
                    pos = titulos.index(titulo)
                    ejemplares[pos]+=1
                    print(f"La cantidad actualizada de ejemplares de {titulo} es de: {ejemplares[pos]}")
                else:
                    print("No poseemos ese titulo en nuestro catalogo ")
            if act == "P":
                titulo = input("ingrese el nombre del titulo que desea pedir prestado ").strip()
                if titulo in titulos:
                    pos = titulos.index(titulo)
                    ejemplar = ejemplares[pos]
                    if ejemplar == 0:
                        print("Ese Titulo esta agotado")
                    else:
                        ejemplares[pos]-=1
                        print(f" La cantidad de ejemplares de {titulo} es de: {ejemplares[pos]}")
                            
                else: 
                    print("No poseemos ese titulo en nuestro catalogo")
            
        case 8:
            print("Hasta Luego!")
            salida = True

                            





