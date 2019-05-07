def cuadrados(lista):

    if not lista:
        return 0

    else:
        return [x*x for x in lista]


print(cuadrados([1,2,3,4]))