# Entradas y valores
n = int(input("Dime las dimensiones de la matriz cuadrada: "))
M = []
f = 0
c = 0
latino = True

# Creación de la matriz
for fila in range(n):
    M.append([0] * n)

# Entradas de la matriz
for fila in range(n):
    for columna in range(n):
        M[fila][columna] = int(input("Dame el valor ({0}, {1}): ". format(fila, columna)))
        if M[fila][columna] < 1 or M[fila][columna] > n:
            latino = False
print(M[f][f+1:n])
# Latino?
while latino:
    if M[f] in M[f][f+1:n]:
        latino = False
        print(latino, "2")
    M_0 =[]
    unico =[]
    for fila in range(1, n):
        M_0.append(M[fila][c])
    for elemt in M_0:
        if elemt not in unico:
            unico.append(elemt)
        else:
            latino = False
        print(latino, "3")

    c += 1
    f += 1
if latino:
    print("Es latino")
else:
    print("No lo es")
