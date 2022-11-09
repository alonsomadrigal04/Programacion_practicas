# entradas y variables
cadena = input("Dime una frase: ")
cadena_2 = ""
palabra = ""
anterior = " "
cont = 2

# bucle
for letra in cadena:
    if letra != " ":  # Es letra
        palabra += letra
    elif anterior != " ":
        if len(palabra) >= 2:  # Poner palabra modificada + espacio
            cadena_2 += palabra
            cadena_2 += palabra[-2:] + " "
            palabra += ""
        else:
            cadena_2 += palabra
        palabra = ""
    else:
        cadena_2 += " "
    anterior = letra
if cadena[-1] != " ":
    cadena_2 += palabra
    cadena_2 += palabra[-2:]
print(cadena_2)

