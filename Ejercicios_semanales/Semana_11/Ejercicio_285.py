# Valores
cadena = "TRWAGMYFPDXBNJZSQVHLCKE"


# Funciones
def letra_dni():
    resto = num % 23
    letra = cadena[resto]
    return letra


def comprueba_letra_dni():
    letra = letra_dni()
    if letra != let:
        return "No es la letra correspondiente"
    return "Es la letra correspondiente"


# Entrada
num = int(input("Dime el numero de tu DNI: "))
let = input("Dime la letra de tu DNI: ")
print(comprueba_letra_dni())
