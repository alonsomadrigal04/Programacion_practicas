l = []
lista1 = [[1, 2], [3, 4]]
for f in range(len(lista1)):
    l.append([0] * len(lista1[0]))
print(l)
for f in range(len(l)):
    for c in range(len(l[0])):
        l[f][c] = lista1[f][c] * 2
for f in range(len(l)):
    for c in range(len(l[0])):
        print(l[f][c], end=" ")
    print()
