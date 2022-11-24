from modulo_test import test

def sumar_lista_digitos (lista1, lista2):
    cont = len(lista1) -1
    cont2 = len(lista2) -1
    dig = 0
    dig2 = 0
    if cont != cont2:
        lista_final = None
    else:
        for num in lista1:
            dig += num * 10 ** cont
            cont -= 1
        for num in lista2:
            dig2 += num * 10 ** cont2
            cont2 -= 1
        n = dig + dig2
        lista_final = []
        while n > 0:
            resto = n % 10
            n //= 10
            lista_final = [resto] + lista_final
    return lista_final

# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(sumar_lista_digitos([3,5,4], [1,6,3]) == [5,1,7])
    test(sumar_lista_digitos([9,9,9], [9,9,9]) == [1,9,9,8])
    test(sumar_lista_digitos([9,9,9], [1]) == None)
    test(sumar_lista_digitos([], [9,9,9]) == None)
    test(sumar_lista_digitos([7,9,9,9], [2,0,0,0]) == [9,9,9,9])
    test(sumar_lista_digitos([9,9,9,9], [2,0,0,0]) == [1,1,9,9,9])
