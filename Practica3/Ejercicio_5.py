n = int(input("Dame un número y te lo escribiré en una lista: "))
lista = []
while n > 0:
    resto = n % 10
    n //= 10
    lista = [resto] + lista
print(lista)
