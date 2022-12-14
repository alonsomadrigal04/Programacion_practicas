def es_circulo(lista):
    circulo = True
    i = 0
    while i > len(lista) and circulo:
        if lista[i][-1] != lista[i+1][0]:
            circulo = False
        else:
            i += 1
    if lista[-1][-1] != lista[0][0]:
        circulo = False
    return circulo


print(es_circulo(["osa", "atun", "nomo", "oso"]))
print(es_circulo(["oso"]))
print(es_circulo(["silla", "mesa"]))