close = "GO"
try:
    a,b = input("Ingrese la primer variable y luego separado por espacios la segunda ").split()
except ValueError:
    print("Error: Debe ingresar dos valores separados por un espacio.")
    close = "FIN"
while(close == "GO"):
    
    print("Este Programa Calculara la tabla de verdad de las variables que usted ingrese \n ")
    
    Expresion = int(input("Ingrese 1 para ver la tabla AND, 2 para ver la tabla OR, 3 para ver la tabla XOR y 4 para ver la tabla NAND  "))
    match(Expresion):
        case 1:
            print(f"{a} * {b} en tabla de verdad equivale a: \n")
            print(f"{a} | {b} | {a} AND {b}")
            print("-" * 17)
            for x in [0, 1]:
                for y in [0, 1]:
                    print(f" {x} | {y} |   {x & y}")
        case 2:
            print(f"{a} + {b} en tabla de verdad equivale a: \n")
            print(f"{a} | {b} | {a} OR {b}")
            print("-" * 16)
            for x in [0, 1]:
                for y in [0, 1]:
                    print(f" {x} | {y} |   {x | y}")
        case 3:
            print(f"{a} XOR {b} en tabla de verdad equivale a: \n")
            print(f"{a} | {b} | {a} XOR {b}")   
            print("-" * 18)
            for x in [0, 1]:
                for y in [0, 1]:
                    print(f" {x} | {y} |   {x ^ y}")
        case 4:
            print(f"{a} NAND {b} en tabla de verdad equivale a: \n")
            print(f"{a} | {b} | {a} NAND {b}")
            print("-" * 19)
            for x in [0, 1]:    
                for y in [0, 1]:
                    print(f" {x} | {y} |   {int(not(x & y))}")
    close = input("Ingrese FIN para terminar o GO para otro intento ").upper()
print("Programa Terminado")