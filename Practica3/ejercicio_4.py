from random import *

# Crear cadena de numeros
cadena = ""
while len(cadena) != 4:
    digito = str(randint(1, 9))
    while digito in cadena:
        digito = str(randint(1, 9))
    cadena += digito

# Bucle principal
res = str(input("Se ha generado un código de cuatro dígitos, ¡intenta acertarlo!: "))
while res != cadena:
    toros = 0
    vacas = 0
    cont = 0
    cont2 = 0
    for numero in cadena:
        cont += 1  # Aquí comprobará la posición del numero original
        for numero_2 in res:
            cont2 += 1  # Aquí la posición del numero dado
            if cont2 > 4:  # si no estaria contando numeros, siempre seria hasta "16".
                cont2 = 1
            if numero == numero_2 and cont == cont2:
                toros += 1
            elif numero == numero_2:
                vacas += 1
    print("\nHas fallado, pero te daré una pista:\nToros {0} | Vacas {1}.".format(toros, vacas))
    res = input("\nIntentalo de nuevo: ")
print("Felicidades, has ganado.")
