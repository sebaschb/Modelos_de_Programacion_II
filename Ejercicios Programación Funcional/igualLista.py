def igualLista(lista1,lista2):
    if len(lista1) == 0:
        return True
    else:
        return igualLista(lista1[1:],lista2[1:]) and lista1[0]==lista2[0]

l1 = [1,2,3,4]
l2 = [2,1,3,4]
print(igualLista(l1,l2))