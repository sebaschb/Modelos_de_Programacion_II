def contarPares(lista):
    if not list:
        return 0

    return len([x for x in lista if x % 2 == 0])


print(contarPares([1, 3, 4, 5, 6, 10, 14, 15, 16, 18]))
