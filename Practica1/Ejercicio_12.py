from math import ceil
# Entrada
horas = int(input("Dame el alquiler del alquiler en horas (Min.:24 h, Max.: 1 mes): "))
dias = ceil(horas/24)
importe = 11
# programa
if horas > 744 or horas < 24:
    print("Entrada no válida")
else:
    if dias == 1:
        print("Tu importe será: {0}€".format(importe))
    elif dias <= 5:
        importe += ((dias-1) * 6)
    elif 14 >= dias > 5:
        dias -= 5
        importe += (4 * 6)
        importe += (dias * 5.5)
    else:
        importe = 110
    print("Tu importe es de: {0}€".format(importe))
