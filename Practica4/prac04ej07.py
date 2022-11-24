from modulo_test import test
from prac04ej02 import divisores


def son_sociables(lista):
    i = 0
    sociables = True
    while i < len(lista) - 1 and sociables:
        div = divisores(lista[i])
        div = div[:-1]
        suma = 0
        for num in div:
            suma += num
        if suma != lista[i + 1]:
            sociables = False
        i += 1
    if sociables:
        div = divisores(lista[-1])
        div = div[:-1]
        suma = 0
        for num in div:
            suma += num
        if suma != lista[0]:
            sociables = False
    return sociables


if __name__ == '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(son_sociables([220, 284]) == True)
    test(son_sociables([14288, 15472, 14536, 14264, 12496]) == True)
    test(son_sociables([14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072,
                        589786, 294896, 358336, 418904, 366556, 274924, 275444,
                        243760, 376736, 381028, 285778, 152990, 122410, 97946,
                        48976, 45946, 22976, 22744, 19916, 17716]) == True)
    test(son_sociables([28158165, 29902635, 30853845, 29971755]) == True)
