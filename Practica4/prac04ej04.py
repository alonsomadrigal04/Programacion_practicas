from modulo_test import test

def contenido_GC(adn):
    suma = 0
    for elem in adn:
        if elem == "G" or elem == "C":
            suma += 1
    porc = round((suma * 100)/len(adn), 2)
    return porc
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(contenido_GC('GCGC') == 100.0)
    test(contenido_GC('CGCG') == 100.0)
    test(contenido_GC('GACGAC') == 66.67)
    test(contenido_GC('TACGTACGTAT') == 36.36)
    test(contenido_GC('CAGTACTACCTCAGACGT') == 50.0)
    test(contenido_GC('GATCGATCGATGCTAGCTAGCGCATC') == 53.85)
