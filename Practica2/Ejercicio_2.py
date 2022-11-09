n = int(input("Dame un número: "))

raiz = 1
while raiz**2 <= n:
    raiz +=1
print(raiz - 1)