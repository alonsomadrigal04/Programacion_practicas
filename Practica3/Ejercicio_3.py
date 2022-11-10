# Entradas
cadena = input("Dame una cadena: ")
cadena_2 = input("Dame OTRA cadena: ")
estar = False
i = 0
# Bucle
while i < len(cadena_2) and not estar:
    if cadena_2[i:i+len(cadena)] == cadena:
        estar = True
    else:
        i += 1
if estar:
    print(True)
else:
    print(False)
