
print("Ejercicio 1:     \n ")

edad = int(input("Ingrese su edad:"))
if edad>=18 :
    print("Usted es mayor de edad")
else:
    print("usted es menor de edad")



print("Ejercicio 2:      \n ")

nota = int(input("Ingrese su nota:   "))
if nota>=6:
    print("Aprobado")
else: 
    print("Desaprobado")


print("Ejercicio 3:        \n ")

npar = int(input("Ingrese un numero par"))
if npar %2 ==0 : 
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


print("Ejercicio 4:     \n ")

edad = int(input("Ingrese su edad"))
if edad>=0 and edad<12:
    print("Usted es un niño")
elif edad>=12 and edad<18:
    print("Usted es un adolescente")
elif edad>=18 and edad<30:
    print("USted es un adulto joven")
else:
    print("Usted es un adulto")


print("Ejercicio 5:      \n ")

password = input("Ingrese una contraseña que posea entre 8 y 14 caracteres")
if len(password) in range(8,14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")




print("Ejercicio 6:     \n ")


from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

nmedian = median(numeros_aleatorios)
nmean = mean(numeros_aleatorios)
nmode = mode(numeros_aleatorios)

if nmean> nmedian and nmedian> nmode:
    print("Hay sesgo positivo")
elif nmean< nmedian and nmedian<nmode:
    print("Hay sesgo negativo")
elif nmean == nmedian and nmedian == nmode:
    print("no hay sesgo")
else:
    print("no se pudo calcular la tendecia")


print("Ejercicio 7         \n ")

palabra = input("ingrese una frase o palabra que desee  ")
uletra = palabra[-1]
uletra = uletra.lower()
if uletra in "aeiou":
    palabra = palabra + "!"
    print(palabra)
else:
    print(palabra)



print("Ejercicio 8:         \n ")


nombre = input("Ingrese su nombre \n ")

opcion = int(input("elija una opcion entre 1, 2 y 3 \n "))

if opcion == 1:
    nombre = nombre.upper()
    print(nombre)
elif opcion == 2:
    nombre = nombre.lower()
    print(nombre)
elif opcion == 3:
    nombre = nombre.title()
    print(nombre)
else:
    print("opcion incorrecta")



print("Ejercicio 9:         \n   ")


magnitud = float(input("Ingrese la magnitud del sismo"))
if magnitud <3:
    print("Muy leve")
elif magnitud >=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud <6:
    print("Fuerte")
elif magnitud>=6 and magnitud <7:
    print("Muy fuerte")
else: 
    print("Extremo")



print("Ejercicio 10:           \n ")



hem,mes,dia = input("Ingrese en que hemisferio se encuentra S/N, el mes y el dia actual, en ese orden separados por espacios  \n  ").split()
hem = hem.upper()
mes = mes.lower()
dia = int(dia)


if mes=="diciembre":
    if dia>=21:
        if hem=="N":
            print("Es Invierno")
        else:
            print("Es Verano")
    else:
        if hem=="N":
            print("Es Otoño")
        else:
            print("Es Primavera")

elif mes =="marzo":
    if dia>=21:
        if hem=="N":
            print("Es Primavera")
        else:
            print("Es Otoño")
    else:
        if hem=="N":
            print("Es Invierno")
        else:
            print("Es Verano")
elif mes=="junio":
    if dia>=21:
        if hem=="N":
            print("Es Verano")
        else:
            print("Es Invierno")
    else:
        if hem=="N":
            print("Es Primavera")
        else:
            print("Es Otoño")
elif mes == "diciembre":
    if dia>=21:
        if hem=="N":
            print("Es Otoño")
        else:
            print("Es Primavera")
    else:
        if hem=="N":
            print("Es Verano")
        else:
            print("Es Invierno")
elif mes in ("enero","febrero"):
    if hem=="N":
        print("Es Invierno")
    else:
        print("Es Verano")
elif mes in("abril","mayo"):
    if hem=="N":
        print("Es Primavera")
    else:
        print("Es Otoño")
elif mes in("julio","agosto"):
    if hem=="N":
        print("Es Verano")
    else:
        print("Es Invierno")
elif mes in("octubre","noviembre"):
    if hem=="N":
        print("Es Otoño")
    else:
        print("Es Primavera")
else:
    print("Datos incorrectos")