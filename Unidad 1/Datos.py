
print("Ejercicio 1:  \n ")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

print("Ejercicio 2:  \n ")

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)



print("Ejercicio 3:  \n ")
# El comando keys() permite trabajar solo con las palabras clave del diccionario
Lista = list(precios_frutas.keys())
print(Lista)

print("Ejercicio 4:  \n ")

contactos = {}

for i in range (5):
    nombre = input("Ingrese nombre de contacto ").capitalize()
    numero = int(input("ingrese el numero de contacto "))
    contactos[nombre] = numero

NConsulta = input("ingrese el nombre de la persona de la que desea consultar el numero ").capitalize()

if (contactos[NConsulta]):
    print (f"El numero de {NConsulta} es:", contactos[NConsulta])
else:
    print("No poseemos el numero de esa persona")


print("Ejercicio 5:  \n ")
from collections import Counter

palabras = input("Ingrese la frase con las palabras deseadas ").split()

Recuento = Counter(palabras)
Unicas = set(palabras)

print("El conteo es: " ,Recuento)
print("El grupo de palabras unicas es: ",Unicas)


print("Ejercicio 6:  \n ")

alumnos = {}
notas = []

for a in range(3):
    nombre = input("ingrese nombre alumno ")
    for n in range(3):
        nota = int(input(f"ingrese nota N° {n+1} "))
        notas.append(nota)
    notas = tuple(notas)
    alumnos[nombre] = notas
    notas = []

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f" {nombre} : promedio = {promedio:.2f}")

print("Ejercicio 7:  \n ")

set1 = {1,3,5,6,8,9}
set2 = {2,3,4,7,8,9}

print("Los estudiantes que aprobaron ambos parciales son: ")
print(set1 & set2)

print("Los estudiantes que aprobaron solo uno de los dos parciales son: ")
print(set1 ^ set2)

print("Los estudiantes que aprobaron almenos un parcial son: ")
print(set1 | set2)


print("Ejercicio 8:  \n ")

DicProd = {"Banana": 50, "Pera": 30, "Manzana": 20}

Consulta = input("Ingrese el producto que desea consultar ").capitalize()

if Consulta in DicProd :
    print (DicProd[Consulta])
    unidades = int(input("ingrese cuantas unidades desea agregar al producto: "))
    DicProd[Consulta] += unidades
else:
    DicProd[Consulta]= int(input("Ingrese cuantas unidades posee del nuevo producto: "))

print("La Lista de productos actalizada es: ",DicProd)

    
print("Ejercicio 9:  \n ")

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
agenda = {
    ("Lunes","10:00"): "Reunion",
    ("Lunes","15:00"): "Entrevista",
    ("Miercoles","12:00"): "Partido",
    ("Viernes","11:00"): "Clase Ingles"
    
}

dia = input("Ingrese el dia que desea consultar en la agenda ").capitalize()
hora = int(input("Ingrese la hora que desea consultar "))



if dia in dias and hora in range(24):
    hora = str(hora) + ":00"
    EvConsulta = (dia,hora)
    if EvConsulta in agenda:
        print("El evento agendado es: ",agenda[EvConsulta])
    else:
        print("No posee eventos en ese momento")


print("Ejercicio 10:  \n ")

Dic1 = {"Argentina":"Buenos Aires","España":"Madrid","Japon":"Tokyo"}
Dic2 = {}
for pais in Dic1:
    capital = Dic1[pais]
    Dic2[capital] = pais

print(Dic1)
print(Dic2)
