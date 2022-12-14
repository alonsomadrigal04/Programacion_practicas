from modulo_test import test


def divisores(n):
    res = []
    for num in range(1, n//2 + 1):
        if n % num == 0:
            res.append(num)
    res.append(n)
    return res


if __name__ == '__main__':
    # Código para ejecutar la función con los datos de prueba
    #    ¡¡SE PUEDE COMENTAR LÍNEAS PERO NO MODIFICARLAS!!    
    test(divisores(1) == [1])
    test(divisores(10) == [1, 2, 5, 10])
    test(divisores(9) == [1, 3, 9])
    test(divisores(10) == [1, 2, 5, 10])
    test(divisores(30) == [1, 2, 3, 5, 6, 10, 15, 30])
    test(divisores(35) == [1, 5, 7, 35])
    test(divisores(49) == [1, 7, 49])
