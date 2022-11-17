def es_perfecto(n):
    for i in range(1, int(n)):
        sumatorio = 0
        if n % i == 0:
            sumatorio += i
    return sumatorio == n


# Entradas
lista = []
numero = int(input("Dame un numero (intro para acabar): "))
lista.append(numero)
while numero != "":
    numero = input("Dame otro más: ")
    lista.append(numero)
    if numero == "":
        lista.remove(numero)

# Procedimiento
lista_final = []
for num in lista:
    if es_perfecto(num):
        lista_final.append(num)
print(lista_final)
