n = int(input("Dame un número entero: "))
M = []
for f in range(n):
    M.append([0]*n)
for fila in range(n):
    for columna in range(n):
        M[fila][columna] = columna - fila
print(M)
