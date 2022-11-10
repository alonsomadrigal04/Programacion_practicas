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

# Latino?
while latino:
    if M[f][c] < 1 or M[f][c] > n:
        latino = False
    if M[f] in M[f][f:n]:
        latino = False
    for columna in range(n):
        