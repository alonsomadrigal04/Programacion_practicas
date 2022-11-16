# Funciones
def media_num():
    media = num // len(str(num))
    if num == 0:
        return 0
    return media


# entradas
num = int(input("Dame una cadena de número: "))
print(media_num())
