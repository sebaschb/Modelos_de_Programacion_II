def mayor(lista):

    if not lista:
        return 0

    if lista[0] > mayor(lista[1:]):
        return lista[0]
    else:
        return mayor(lista[1:])


print(mayor([-1,2,-3,-4]))
