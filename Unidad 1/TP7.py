
print("Ejercicio 1:     \n    ")


def CalFact(n):
    if n == 1:
        return 1
    else:
        return (n*CalFact(n-1))
    
numFa= int(input("Ingrese el numero del cual desea saber su factorial"))

for i in range(1,numFa+1):
    print(f"El factorial de {i} es: ",CalFact(i))
    



print("Ejercicio 2:     \n    ")

def CalFibo(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return (CalFibo(n-1)+ CalFibo(n-2))
    
numFi = int(input("ingrese la posicion que desea de Fibonacci"))

print(f" El fibonacci de {numFi} es : ",CalFibo(numFi),"\n")

for i in range(1,numFi):
    print(f" El fibonacci de {i} es : ",CalFibo(i))



print("Ejercicio 3:     \n    ")


def CalPot(n,m):
    if m == 1:
        return n
    else:
        return n* CalPot(n,m-1)
    
numPot = int(input("ingrese un numero "))
Potencia = int(input("ingrese la potencia a la que desea elevarlo "))

if Potencia >=1:
    resultadoP = CalPot(numPot,Potencia)
    print(f" El resultado de {numPot} elevado a {Potencia} es:", resultadoP)
elif Potencia == 0:
    print(f"El resultado de {numPot} elevado a {Potencia} es:",1)
else:
    print("No se permiten potencias negativas")


print("Ejercicio 4:     \n    ")

def ConverBinario(n):
    if n ==0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return ConverBinario(n//2) + str(n%2)

numDec= int(input("ingrese el numero que desea convertir a binario "))

print("el resultado es: ",ConverBinario(numDec))




print("Ejercicio 5:     \n    ")

def CalPol(cadena):
    if len(cadena)<=1:
        return True
    elif cadena[0] != cadena[-1]:
        return False
    else:
        # achicamos la cadena por el lado izquierdo y el derecho, asi la vamos recorriendo a la par.
        return CalPol(cadena[1:-1])
    
cadena= input("ingrese sin comas ni espacios la cadena que desea saber si es polindromo ").lower()

if CalPol(cadena) == True:
    print(f"{cadena} es polindromo")
else:
    print(f"{cadena} no es polindromo")




print("Ejercicio 6:     \n    ")

def SumDigitos(n):
    if n<=9:
        return n
    else:
        return (SumDigitos(n//10) + (n%10))
    

numDig = int(input("Ingrese el numero del cual desea sumar sus digitos "))

if numDig>=0:
    print(f" La suma de los digitos de {numDig} es : ",SumDigitos(numDig))
else:
    # en caso de que el numero sea negativo lo convertimos a positivo
    # ya que la finalidad es sumarlos sin importar su signo
    print(f" La suma de los digitos de {numDig} es : ",SumDigitos(-numDig))




print("Ejercicio 7:     \n    ")

def ConBloques(n):
    if n == 1:
        return 1
    else:
        return ConBloques(n-1) +n


NumInicio = int(input("Ingrese el numero de bloques iniciales en la base "))

print("El numero total de bloques es:",ConBloques(NumInicio))



print("Ejercicio 8:     \n    ")

def ConRep(num,dig):
    if num<=9:
        if num==dig:
            return 1
        else:
            return 0
    else:
        ultimo = num%10
        if ultimo == dig:
            return 1+ ConRep(num//10,dig)
        else:
            return ConRep(num//10,dig)

NumCont = int(input("Ingrese el numero a evaluar"))
digito = int(input("ingrese el digito que quiere saber cuantas veces se repite"))

print(f"El digito {digito} se repite en {NumCont} ",ConRep(NumCont,digito)," veces")