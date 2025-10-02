print("Ejercicio 1:  \n ")

def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()


print("Ejercicio 2:  \n ")
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
saludar_usuario("Marcos")

print("Ejercicio 3:  \n ")

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

us_nom,us_ape,us_ed,us_res = input("Ingrese su nombre, apellido, edad y residencia separados por espacio ").split()
informacion_personal(us_nom,us_ape,us_ed,us_res)

print("Ejercicio 4:  \n ")

import math

def area_circulo(radio):
    ar_cir = math.pi * (radio**2)
    return ar_cir
def perim_circulo(radio):
    per_cir = (2*math.pi)*radio
    return per_cir

r_circulo = int(input("ingrese el radio del circulo "))
area = round(area_circulo(r_circulo),2)
perimetro = round(perim_circulo(r_circulo),2)
print(f"El area del circulo es: {area} y el perimetro es: {perimetro} ")

print("Ejercicio 5:  \n ")

def segundos_a_horas(seg):
    hora = seg/3600
    hora = round(hora,2)
    return hora

segundos = int(input("ingrese la cantidad de segundos que desea convertir a horas "))

horas = segundos_a_horas(segundos)
print(f" {segundos} segundos equivalen a {horas} horas ")


print("Ejercicio 6:  \n ")

def tabla_multiplicar(num):
    tabla = []
    for i in range(11):
        res= num*i
        tabla.append(res)
    return tabla
num = int(input("ingrese el numero que desea saber su tabla de multiplicar "))
resultado = tabla_multiplicar(num)
print(f"La tabla de Multiplicar de {num} es : \n {resultado}")


print("Ejercicio 7:  \n ")

def operaciones_basicas(a,b):
    tupla = (f"Suma: {a+b} Resta: {a-b} Multiplicacion: {a*b} Division: {a/b}")
    return tupla

num1 = int(input("ingrese el primer numero "))
num2 = int(input("Ingrese el segundo numero "))

resultado = operaciones_basicas(num1,num2)
print(f"Los resultados Operando {num1} y {num2} son: ")
print(resultado)



print("Ejercicio 8:  \n ")

def calcular_imc(peso,altura):
    imc = peso/(altura**2)
    imc = round(imc,2)
    return imc
peso = float(input("Ingrese su peso en kilogramos "))
altura = float(input("Ingrese su altura en metros "))

imc = calcular_imc(peso,altura)
print(f"Su imc es de: {imc}")


print("Ejercicio 9:  \n ")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5)+32
    fahrenheit = round(fahrenheit,2)
    return fahrenheit

gradosC = float(input("ingrese la temperatura en grados Celsius "))

gradosF = celsius_a_fahrenheit(gradosC)
print(f" La temperatura en grados fahrenheit es de: {gradosF} ")

print("Ejercicio 10:  \n ")

def calcular_promedio(a,b,c):
    res= (a+b+c)/3
    res = float(round(res,2))
    return res

num1 = int(input("Ingrese el primer numero "))
num2 = int(input("Ingrese el segundo numero "))
num3 = int(input("Ingrese el tercer numero "))

promedio = calcular_promedio(num1,num2,num3)
print(f" El promedio es : {promedio}")