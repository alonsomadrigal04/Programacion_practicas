# Funcion
def nombres(lista, inicial):
    lista_inicial = []
    for nombre in lista:
        if inicial == nombre[:1]:
            lista_inicial.append(nombre)
    return lista_inicial

# Entrada
lista = []
nombre = input("Dame un nombre (intro para acabar): ")
lista.append(nombre)
while nombre != "":
    nombre = input("Dame otro más: ")
    lista.append(nombre)
    if nombre == "":
        lista.remove(nombre)
inicial = input("Ahora dame una inical: ")

# Llamada
print(nombres(lista, inicial))

