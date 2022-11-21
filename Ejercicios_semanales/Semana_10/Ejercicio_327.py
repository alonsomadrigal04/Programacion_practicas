def es_perfecto(n):
    sumatorio = 0
    for i in range(1, int(n)):
        if int(n) % i == 0:
            sumatorio += i
    return sumatorio == n


# Entradas
lista = []
n = int(input("Dame un numero (intro para acabar): "))
lista.append(n)
while n != "":
    n = input("Dame otro más: ")
    lista.append(n)
    if n == "":
        lista.remove(n)

# Procedimiento
lista_final = []
for num in lista:
    if es_perfecto(int(num)):
        lista_final.append(num)
print(lista_final)
