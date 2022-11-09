n = int(input("Dame un número y te lo escribiré en una lista: "))
lista = []
t = 0
p = 0
while n > 0:
    resto = n % 10
    n //= 10
    lista = [resto] + lista
for elemento in lista:
    t = elemento * (10 ** p)
n_2 = int(input("Dame otro numero: "))
lista_2 = []
while n_2 > 0:
    resto = n_2 % 10
    n_2 //= 10
    lista = [resto] + lista
