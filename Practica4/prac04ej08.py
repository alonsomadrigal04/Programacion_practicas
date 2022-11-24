from modulo_test import test

def crear_lista_digitos (n, lista):
    while n > 0:
        resto = n % 10
        n //= 10
        lista = [resto] + lista
    print(lista)
    return lista


# –- Programa principal –-
lista = []
num = int(input("Ve dandome numeros (0 o menor para terminar): "))
while num > 0:
    crear_lista_digitos(num, lista)
    num = int(input("Dame otro: "))

# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
#if __name__== '__main__':
    # El código del programa principal debe ir aquí
    
