
print("Ejercicio 1:           \n ")

for i in range(101):
    print(i)


print("Ejercicio 2:           \n ")

numdig = input("  ingrese un numero para calcular sus digitos    \n")
digitos = len(numdig)
print(f"el numero {numdig} posee {digitos} digitos")


print("Ejercicio 3:           \n ")

num1 = int(input(" ingrese el limite inferior  "))
num2 = int(input(" ingrese el limite superior  "))
suma = 0
for i in range(num1+1,num2):
    suma += i
print(f"la suma es: ",suma)



print("Ejercicio 4:           \n ")
suma=0
num=-1
while num != 0:
    num = int(input(" ingrese un numero "))
    suma +=num
print(" La suma es: ",suma)


print("Ejercicio 5:           \n ")
import random
num = random.randint(1,9)
intento = 0
while(intento != num):
    intento=int(input("intente adivinar el numero al azar entre 1 y 9 \n "))
print(" Felicidades! ")

print("Ejercicio 6:           \n ")

for i in range(100,-1,-2):
    print(i)



print("Ejercicio 7:           \n ")

num = int(input("escriba un numero entero positivo "))
suma=0
for i in range(0,num):
    suma +=i
print(f" La suma total es de : {suma}")

print("Ejercicio 8:           \n ")
pares=0
impares=0
positivos=0
negativos=0
for i in range(0,100):
    num = int(input(" ingrese el numero \n "))
    if num % 2 == 0:
        pares += 1
    else:
        impares+= 1
    if num >0:
        positivos +=1
    elif num<0:
        negativos +=1
print(f" La cantidad de pares es: {pares} y la cantidad de impares es: {impares} \n ")
print(f" La cantidad de positivos es: {positivos} y la de negativos es: {negativos} ")




print("Ejercicio 9:           \n ")
promedio= 0
suma=0
for i in range(0,100):
    num = int(input("ingrese un numero"))
    suma+=num
promedio= suma/100
print(f" El promedio es:  {promedio}")




print("Ejercicio 10:           \n ")

numa = input(" Ingrese el numero que desea invertir")
numa = numa[::-1]
numa = int(numa)
print(" El numero invertido es:  ",numa)