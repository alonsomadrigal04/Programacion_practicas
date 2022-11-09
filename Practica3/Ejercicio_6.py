# Entradas y variables
n = int(input("Dame un número, (enter para terminar): "))
lista = [n]
while n != "":
    n = str(input("Dame otro numero: "))
    lista.append(n)
    if n == "":
        lista.remove(n)
# mostrar lista y numero
print(lista)
for elemento in lista:
    print(elemento, end="")
