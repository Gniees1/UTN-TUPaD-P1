
print("Ejercicio 1:     \n    ")

ListaNotas = [6,3,7,8,10,7,5,9,5,4,5,6,7]

print("Lista Completa: ",ListaNotas,"\n ")

suma= 0
for nota in ListaNotas:
    suma += nota

promedio = suma / len(ListaNotas)
promedio = round(promedio,2)
print(" El promedio de las notas es: ",promedio)

NotaMayor = -500
NotaMenor = 500

for nota in ListaNotas:
    if nota> NotaMayor:
        NotaMayor = nota
    elif nota < NotaMenor:
        NotaMenor = nota

print(f"\n La nota mayor es: {NotaMayor} y la nota menor es: {NotaMenor} \n ")



print("Ejercicio 2:       \n    ")


Lista = []

for i in range(5):
    elemento = input(f"ingrese el elemento {i+1}: \n ").lower()
    
    Lista.append(elemento)

Lista = sorted(Lista)
print (" La Lista ordenada es: " ,Lista)

RemProd = input("ingrese el elemento que desea quitar de la lista ").lower()

Lista.remove(RemProd)
print(" La lista actualizada es: ", Lista)






print("Ejercicio 3:       \n    ")
import random


ListaNumeros = []
ListaPares = []
ListaImpares = []
for i in range(15):
    numero = random.randint(1,100)
    ListaNumeros.append(numero)


for numero in ListaNumeros:
    if numero %2  == 0:
        ListaPares.append(numero)
    else:
        ListaImpares.append(numero)

print(" La cantidad de valores en la lista par es de : ",len(ListaPares))
print (" La cantidad de valores en la lista impar es de: ", len(ListaImpares))



print("Ejercicio 4:       \n    ")


datos = [1,3,5,3,7,1,9,5,3]
SinRepetir = []

for numero in datos:
    if numero not in SinRepetir:
        SinRepetir.append(numero)

print(" La lista sin repeticiones es : ", SinRepetir)




print("Ejercicio 5:       \n    ")

ListaEstudiantes = ["Juan","Pedro","Pepe","Jose","Felipe","Felix","Mateo","Luca"]

valor = int(input(" Ingrese 1 si desea agregar un nuevo estudiante o 2 si desea eliminar a alguno de la lista "))

match valor:
    case 1:
        NuevoEstudiante = input(" ingrese el nuevo estudiante")
        ListaEstudiantes.append(NuevoEstudiante)
    case 2:
        QuitarEstudiante = input(" ingrese el nombre del estudiante a quitar:   ").capitalize()
        ListaEstudiantes.remove(QuitarEstudiante)
print(" La lista actualizada es: ",ListaEstudiantes)




print("Ejercicio 6:       \n    ")



ListaRot = [1,2,3,4,5,6,7]
hold = ListaRot[-1]
print("Lista Original   ",ListaRot)
for i in range(len(ListaRot)-1,-1,-1):
    ListaRot[i] = ListaRot[i-1]

ListaRot[0] = hold
print(" Lista Modificada",ListaRot)



print("Ejercicio 7:       \n    ")
Dias = ["Lunes","Martes","Miercoles","Jueves","viernes","Sabado","Domingo"]
ListaTemps = [[12,9,13,15,17,15,11],[18,17,22,27,28,31,30]]
AmpTermica = 0
cont = 0
DiaMax = 0
ProMin = 0
ProMax = 0

# Se investigo la funcion zip que permite recorrer dos listas distintas en paralelo.
# En este caso *ListaTemps desempaqueta las listas dejandolas como dos argumentos ([1,2,3],[4,5,6]).
for a, b in zip(*ListaTemps): 
    ProMin += a
    ProMax += b
    if (b-a) > AmpTermica:
        AmpTermica = b-a
        DiaMax = Dias[cont]
    cont +=1
ProMin = round(ProMin/7,2)
ProMax = round(ProMax/7,2)
print(f" El promedio de temperaturas minimas en la semana es de:   {ProMin} \n ")
print(f" El promedio de temperaturas maximas en la semana es de:   {ProMax} \n")

print(f" La mayor amplitud termica se dio el dia:  {DiaMax} y fue de:  {AmpTermica} grados")



print("Ejercicio 8:       \n    ")

NotasAlumnos = [[7,6,4],[3,8,9],[5,7,7],[7,6,9],[10,8,8]]

print("Promedio por estudiante: ")

for i in range(len(NotasAlumnos)):
    promedio= sum(NotasAlumnos[i])/len(NotasAlumnos[i])
    promedio = round(promedio,2)
    print(f"El promedio del alumno {i+1} es: ",promedio)

print("Promedio por materia:  ")

NMaterias= len(NotasAlumnos[0])
NAlumnos = len(NotasAlumnos)

for j in range(NMaterias):
    suma = 0
    for i in range(NAlumnos):
        suma += NotasAlumnos[i][j]
    promedio = suma/NAlumnos
    print(f"El promedio de la materia {j+1} es de: {promedio} ")



print("Ejercicio 9:       \n    ")

Tateti = [["-"] * 3 for _ in range(3)]

for fila in Tateti:
    print(" ".join(fila))

simbolo = input("Ingrese el simbolo del primer jugador").upper()

while(simbolo == "O" or simbolo == "X"):
    f,c = map(int,input("Ingrese la posicion de fila y separado con espacio la de columnas").split())
    Tateti[f][c] = simbolo
    for fila in Tateti:
        print(" ".join(fila))
    simbolo= input( "Ingrese el siguiente simbolo a jugar: ").upper()
print(" Juego Terminado! ")

print("Ejercicio 10:       \n    ")


TotalProd= 0 
Productos = ["1","2","3","4"]
Ventas = [[0] * 4 for _ in range(7)]
Mayor = 0
cont = 0
MayorVentasDia = 0
DiaMayor = 0
#Se cargan las ventas de cada Producto.
for i in range(7):
    for j in range(4):
        Ventas[i][j] = cont
        cont+=1

for fila in Ventas:
    print(" ".join(str(valor) for valor in fila))


for j in range(4):  
    TotalProd = 0
    for i in range(7): 
        TotalProd += Ventas[i][j]
    if TotalProd > Mayor:
        Mayor = j
    print(f"Total vendido del producto {j}: {TotalProd}")

print(" El producto mas vendido es el : ",Mayor)


for i, fila in enumerate(Ventas):
    TotalDia = sum(fila)  
    print(f"Total ventas del día {i+1}: {TotalDia}")
    
    if TotalDia > MayorVentasDia:
        MayorVentasDia = TotalDia
        DiaMayor = i+1 

print(f" El día con mayores ventas es el: {DiaMayor} con {MayorVentasDia} ventas.")