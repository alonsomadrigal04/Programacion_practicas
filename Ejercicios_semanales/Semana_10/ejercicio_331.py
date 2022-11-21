# Función lista invertida
def lista_invert(lista):
    lista_invert = []
    for num in range(len(lista)-1, -1, -1):
        lista_invert.append(lista[num])
    return lista_invert


# Creación de lista
lista = []
n = int(input("Dame un numero (intro para acabar): "))
lista.append(n)
while n != "":
    n = input("Dame otro más: ")
    lista.append(n)
    if n == "":
        lista.remove(n)

# Print de la lista inv.
print("Lista original: {0}\nlista invertida: {1}".format(lista, lista_invert(lista)))
