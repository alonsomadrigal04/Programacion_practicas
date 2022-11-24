from modulo_test import test


def expansion_triplete_CAG(adn):
    i = 0
    cont = 0
    mayor = 0
    while i+3 <= len(adn):
        if adn[i:i+3] == "CAG":
            cont += 1
            if cont > mayor:
                mayor = cont
            i += 3
        else:
            cont = 0
            i += 1
    if mayor == 0:
        mayor = None
    return mayor


if __name__ == '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(expansion_triplete_CAG('GACGAC') == None)
    test(expansion_triplete_CAG('CAGCAG') == 2)
    test(expansion_triplete_CAG('TACGTACGTAT') == None)
    test(expansion_triplete_CAG('CAGCAGTACCTCAGACGT') == 2)
    test(expansion_triplete_CAG('GATCGATCGATGCTAGCTAGCGCATC') == None)
    test(expansion_triplete_CAG('TACTCAGCAGGATGCAGCAGCAGCAGCAG') == 5)
