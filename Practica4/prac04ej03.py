from modulo_test import test
from prac04ej02 import divisores
def son_amigos (n1,n2):
        suma1 = 0
        suma2 = 0
        lista1 = divisores(n1)
        lista2 = divisores(n2)
        for num in lista1[:-1]:
                suma1 += num
        for num in lista2[:-1]:
                suma2 += num
        return suma1 == n2 and suma2 == n1
if __name__== '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(son_amigos(30, 42) == False)
    test(son_amigos(42, 30) == False)
    test(son_amigos(220, 284) == True)
    test(son_amigos(284, 220) == True)
    test(son_amigos(2620, 2924) == True)
    test(son_amigos(6368, 6232) == True)
