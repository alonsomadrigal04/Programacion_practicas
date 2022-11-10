# creación lista 1
n = int(input("Dame un número y te lo escribiré en una lista: "))
res1 = n
lista = []
while n > 0:
    resto = n % 10
    n //= 10
    lista = [resto] + lista

# creación lista 2
n_2 = int(input("Dame otro numero: "))
res2 = n_2
lista_2 = []
while n_2 > 0:
    resto = n_2 % 10
    n_2 //= 10
    lista_2 = [resto] + lista_2

# Operación y print
lista_3 = []
n_3 = res1 + res2
while n_3 > 0:
    resto = n_3 % 10
    n_3 //= 10
    lista_3 = [resto] + lista_3
print(lista_3)
