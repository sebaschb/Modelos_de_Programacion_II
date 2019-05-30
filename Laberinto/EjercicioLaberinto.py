class Nodo:
    def __init__(self, valor,arri=None,aba=None,izq=None,der=None):
        self.valor = valor
        self.arri = arri
        self.aba = aba
        self.izq = izq
        self.der = der



def busqueda_matriz(lista, tam, valor):
    if lista == []:
        return []
    else:
        try:
            return [tam - len(lista), lista[0].index(valor)]
        except ValueError:
            pass
        return busqueda_matriz(lista[1:], tam, valor)


def laberinto_arbol(laberinto, pos, listaPadresAbajo, listaPadresArriba, listaPadresDerecha, listaPadresIzquierda):

    print(pos[0],pos[1],'oosldl')
    # abajo
    if len(laberinto) > pos[0] + 1 and pos[0] + 1 > 0 and len(laberinto) > pos[1] and pos[1] > 0 and not isPadre(listaPadresAbajo,[pos[0]+1,pos[1]]) :
        if laberinto[pos[0] + 1][pos[1]] == '0' or laberinto[pos[0] + 1][pos[1]] == 'x' or laberinto[pos[0] + 1][pos[1]] == 'y':
            print("If abajo")
            listaPadresAbajo.append([pos[0]+1, pos[1]])
            print(listaPadresAbajo)
            return Nodo(laberinto[pos[0]][pos[1]], aba = laberinto_arbol(laberinto, [pos[0] + 1, pos[1]],listaPadresAbajo, listaPadresArriba, listaPadresDerecha, listaPadresIzquierda))

    # arriba
    if len(laberinto) > pos[0] - 1 and pos[0] - 1 > 0 and len(laberinto) > pos[1] and pos[1] > 0 and not isPadre(listaPadresArriba, [pos[0] - 1, pos[1]]):
        if laberinto[pos[0] - 1][pos[1]] == '0' or laberinto[pos[0] - 1][pos[1]] == 'x' or laberinto[pos[0] - 1][pos[1]] == 'y':
            print("If arriba")
            listaPadresArriba.append([pos[0]-1, pos[1]])
            print(listaPadresArriba)
            return Nodo(laberinto[pos[0]][pos[1]], arri= laberinto_arbol(laberinto, [pos[0] - 1, pos[1]], listaPadresAbajo, listaPadresArriba, listaPadresDerecha, listaPadresIzquierda))

    # derecha
    if len(laberinto) > pos[1] + 1 and pos[1] + 1 > 0 and len(laberinto) > pos[0] and pos[0] > 0 and not isPadre(listaPadresDerecha, [pos[0],pos[1] + 1]):
        if laberinto[pos[0]][pos[1] + 1] == '0' or laberinto[pos[0]][pos[1] + 1] == 'x' or laberinto[pos[0]][pos[1] + 1] == 'y':
            print("If derecha")
            listaPadresDerecha.append([pos[0], pos[1]+1])
            print(listaPadresDerecha)
            return Nodo(laberinto[pos[0]][pos[1]], der= laberinto_arbol(laberinto, [pos[0],pos[1] + 1], listaPadresAbajo, listaPadresArriba, listaPadresDerecha, listaPadresIzquierda))

    # izquierda
    if len(laberinto) > pos[1] - 1 and pos[1] - 1 > 0 and len(laberinto) > pos[0] and pos[0] > 0 and not isPadre(listaPadresIzquierda, [pos[0],pos[1] - 1]):
        if laberinto[pos[0]][pos[1] - 1] == '0' or laberinto[pos[0]][pos[1] - 1] == 'x' or laberinto[pos[0]][pos[1] - 1] == 'y':
            print("If derecha")
            listaPadresIzquierda.append([pos[0], pos[1]-1])
            print(listaPadresIzquierda)
            return Nodo(laberinto[pos[0]][pos[1]], izq= laberinto_arbol(laberinto, [pos[0],pos[1] - 1], listaPadresAbajo, listaPadresArriba, listaPadresDerecha, listaPadresIzquierda))

    return Nodo(None)

def insertar_nodo(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if valor < arbol.valor:
        return Nodo(arbol.valor,insertar_nodo(arbol.izq,valor),arbol.der)
    if valor > arbol.valor:
        return Nodo(arbol.valor,arbol.izq,insertar_nodo(arbol.der,valor))

def lista_arbol(lista):
    if lista == []:
        return Nodo(None)
    else:
        if len(lista)>1:
            return insertar_nodo(lista_arbol(lista[0:len(lista)-1]), lista[len(lista)-1])
        if len(lista)==1:
            return Nodo(lista[0])

def isPadre(padres,pos):
    try:
        padres.index(pos)
        print(padres)
        return True
    except ValueError:
        pass
    return False

# print(busqueda_matriz([[1,9,3],[4,5,6],[7,8,9]],3,9))
m = [['1', '1', '1','0'], ['0','0', 'x', 'y'], ['0','1', '0', '1'],['1','1', '0', '0']]

print(laberinto_arbol(m, busqueda_matriz(m, 4, 'x'),[],[],[],[]))
