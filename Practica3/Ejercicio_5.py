n = int(input("Dame un número y te lo escribiré en una lista: "))
n_1 = n
lista = []
cont = 0
while n > 0:
    n //= 10
    cont += 1
for i in range(cont+1, 0, -1):
    print(i)
    lista.append(n_1 //(10*i))
print(lista)
mdjd