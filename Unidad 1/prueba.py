titulos = ["el principito","La sirenita","Alicia en el pais de las Maravillas"]
stock = [2,5,7]

for i in titulos:
    pos = titulos.index(i)
    print(i,stock[pos])

print("Opcion 2   ----------  \n ")

for i, valor in enumerate(titulos):
    print(valor,stock[i])