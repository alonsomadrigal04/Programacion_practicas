from modulo_test import test

def es_cuadrado_latino (matriz):
    nf = len(matriz)
    nc = len(matriz[0])
    es_cuadrado_latino = True
    fil = 0
    while fil < nf and es_cuadrado_latino:
        col = 0
        while col < nc and es_cuadrado_latino:
            if matriz[fil][col]<1 or matriz[fil][col]>nf:
                print("El numero", matriz[fil][col], "no es valido")
                es_cuadrado_latino = False
            elif matriz[fil][col] in matriz[fil][col+1:]:
                print("El número", matriz[fil][col], "ya esta en la fila", fil)
                es_cuadrado_latino = False
            else:
                resto_fil = fil+1
                while resto_fil<nf and es_cuadrado_latino:
                    if matriz[fil][col] == matriz[resto_fil][col]:
                        print("el numero", matriz[fil][col], "ya esta en la columna", col)
                        es_cuadrado_latino = False
                    else:
                        resto_fil += 1
            col += 1
        fil += 1
    return es_cuadrado_latino
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!
    matriz2=[[1,2,3], \
             [2,3,1], \
             [3,1,2]]
    matriz3=[[1,2,3,4], \
             [2,1,4,3], \
             [3,4,1,2], \
             [4,3,2,1]]
    matriz4=[[1,2,3,4], \
             [3,4,1,2], \
             [4,3,2,1], \
             [2,1,4,3]]
    matriz5=[[1,2,3], \
             [0,3,1], \
             [3,1,2]]
    matriz6=[[1,2,3], \
             [2,3,4], \
             [3,1,2]]
    matriz7=[[1,2,3], \
             [2,3,1], \
             [1,2,3]]
    matriz8=[[1,2,3,4], \
             [2,1,4,3], \
             [3,4,1,2], \
             [1,3,2,4]]

    test(es_cuadrado_latino(matriz2) == True)
    test(es_cuadrado_latino(matriz3) == True)
    test(es_cuadrado_latino(matriz4) == True)
    test(es_cuadrado_latino(matriz5) == False)
    test(es_cuadrado_latino(matriz6) == False)
    test(es_cuadrado_latino(matriz7) == False)
    test(es_cuadrado_latino(matriz8) == False)
