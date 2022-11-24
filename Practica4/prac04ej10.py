def leer_matriz_enteros():
    n = int(input("Dime la dimensión de la matriz (ha de ser cuadrada): "))
    M = []
    for i in range(n):
        M.append([0] * n)
    for f in range(n):
        for c in range(n):
            M[f][c] = int(input("Dime el valor: {0} {1}: ".format(f, c)))

def mostrar_matriz_enteros(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end=" ")
        print()

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
#if __name__== '__main__':
    # El código del programa principal debe ir aquí

matriz = leer_matriz_enteros()
mostrar_matriz_enteros(matriz)