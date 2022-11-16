# Valores
cadena = "TRWAGMYFPDXBNJZSQVHLCKE"


# funciones
def letra_dni():
    resto = num % 23
    return cadena[resto]


# Programa
num = int(input("Dame tu número de DNI: "))
print(letra_dni())
