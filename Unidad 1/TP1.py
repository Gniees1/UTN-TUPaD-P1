import math

#Ex 1
print("Hola, Mundo!")


#Ex 2
nombre = input("ingrese su nombre")
print(f"Hola {nombre}")

#Ex 3
nombre, apellido, edad, ciudad = input("Ingrese nombre, apellido, edad y ciudad separados por comas: ").split(',')
edad = int(edad)
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}")

#Ex 4

pi = math.pi
radio = int(input("ingrese el radio del circulo"))
area= pi * radio**2
perimetro= 2*pi*radio
print(f"el area de su circulo es: {area} y su perimetro es: {perimetro}")

# ex 5

segundos = int(input("ingrese la cantidad de segundos"))
horas = segundos/3600
print(f"esos segundos equivalen a: {horas} horas")

# Ex 6

n = int(input("ingrese un numero"))
print("su tabla de multiplicar es: ",2*n,3*n,4*n,5*n,6*n,7*n,8*n,9*n)

# Ex 7

a,b = map(int,input("ingrese dos numeros distintos de cero").split())
print("La suma es: ",a+b," la resta es :",a-b, " la multiplicacion es: ",a*b," y la divison es: ",a/b)

# Ex 8

peso, altura = map(float, input("ingrese su peso en kg y su altura en metros").split())
IMC = peso/(altura**2)
print("su indice de masa corporal es de: ", IMC)

# Ex 9

Celsius = float(input("ingrese la temperatura en celsius"))
Fahrenheit = (9/5)*Celsius + 32
print("la temperatura en fahrenheit es de: ",Fahrenheit )

# Ex 10

a,b,c = map(int,input("ingrese 3 numeros ").split())
print("El promedio de los tres es: ",(a+b+c)/3)