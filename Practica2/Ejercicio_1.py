contador = 0
for i in range (1, 111):
    contador += 1
    if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i, end=" ")
    else:
        if i % 3 == 0:
            print("Cosa", end="")
        if i % 5 == 0:
            print("Losa", end="")
        if i % 7 == 0:
            print("Wosa", end="")
        print(" ", end=" ")
    if contador == 11:
        contador = 0
        print("")