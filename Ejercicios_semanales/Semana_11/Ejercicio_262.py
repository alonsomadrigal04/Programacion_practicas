# Funcion
def es_repeticion():
    num = len(cadena)
    cadena_2 = cadena[int(num/2):int(num)]
    if cadena_2 == cadena[0:int(num/2)]:
        return True
    return False


# Entrada
cadena = input("Dame una cadena: ")
print(es_repeticion())
