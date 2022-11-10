# Entradas y valores
n = int(input("Dime las dimensiones de la matriz cuadrada: "))
M = []
Es = False
cont = 0
cont_1 = 0
triangular = True
# Creación de la matriz
for fila in range(n):
    M.append([0] * n)

# Entradas de la matriz
for fila in range(n):
    for columna in range(n):
        M[fila][columna] = int(input("Dame el valor ({0}, {1}): ". format(fila, columna)))

# Comprobación triangular superior
for fila in range(n):
    for columna in range(n):
        if columna - fila < 0:
            cont += 1
            if M[fila][columna] == 0:
                cont_1 += 1
if cont == cont_1:
    print(True)
else:
    print(False)