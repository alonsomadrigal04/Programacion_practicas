#from modulo_test import test
from prac04ej04 import contenido_GC
from prac04ej05 import expansion_triplete_CAG


def menu_ADN(adn):
    print("------------------------------------------------\n(1). Porcentaje de G C de una secuencia\n(2). Máximo número de"
          "repeticiones consecutivas de un patron\n------------------------------------------------\n")
    res = int(input("Elija una opción: "))
    while res not in [1, 2]:
        res = int(input(("Opción no valida, elija de nuevo: ")))
    if res == 1:
        print(contenido_GC(adn))
    elif res == 2:
        print(expansion_triplete_CAG(adn))
    return



# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
#if __name__== '__main__':
    # El código del programa principal debe ir aquí

adn = input("Escriba su secuencia de adn: ")
menu_ADN(adn)
