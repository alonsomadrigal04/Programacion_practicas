# Entradas
cadena = input("Dame una cadena: ")
cadena_2 = input("Dame OTRA cadena: ")
estar = False

# Bucle
for i in range(len(cadena_2)):
    if cadena == cadena_2[i:i+len(cadena)]:
        estar = True
if estar:
    print(True)
else:
    print(False)
