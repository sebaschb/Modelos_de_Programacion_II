def listaOrdenada(lista):
    if len(lista) == 0 :
        return True
    else:
        return lista[0]<=lista[1] and listaOrdenada(lista[2:])

