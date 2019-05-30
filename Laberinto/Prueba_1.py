class Nodo:
    def __int__(self, valor, hijos=[]):
        self.valor = valor
        self.hijos = hijos


def busqueda_matriz(lista, tam, valor):
    if lista == []:
        return []
    else:
        try:
            return [tam - len(lista), lista[0].index(valor)]
        except ValueError:
            pass
        return busqueda_matriz(lista[1:], tam, valor)


def laberinto_arbol(laberinto, pos, listaPadres):

    print(pos[0],pos[1],'oosldl')
    listaPadres.append([pos[0],pos[1]])
    # abajo
    if len(laberinto) > pos[0] + 1 and pos[0] + 1 > 0 and len(laberinto) > pos[1] and pos[1] > 0 and not isPadre(listaPadres,[pos[0]+1,pos[1]]) :
        if laberinto[pos[0] + 1][pos[1]] == '0' or laberinto[pos[0] + 1][pos[1]] == 'x' or laberinto[pos[0] + 1][pos[1]] == 'y':
            print("If abajo")
            return Nodo(laberinto[pos[0]][pos[1]], laberinto_arbol(laberinto, [pos[0] + 1, pos[1]],listaPadres))

    # arriba
    if pos[0] - 1 > 0 and pos[1] > 0:
        if laberinto[pos[0] - 1][pos[1]] == '0' or laberinto[pos[0] - 1][pos[1]] == 'x' or laberinto[pos[0] - 1][pos[1]] == 'y':
            print("If arriba")
            return Nodo(laberinto[pos[0]][pos[1]], laberinto_arbol(laberinto, [pos[0] - 1, pos[1]],listaPadres))

    # derecha
    if pos[0] > 0 and pos[1] + 1 >0:
        if laberinto[pos[0]][pos[1] + 1] == '0' or laberinto[pos[0]][pos[1] + 1] == 'x' or laberinto[pos[0]][pos[1] + 1] == 'y':
            print("If derecha")
            return Nodo(laberinto[pos[0]][pos[1]], laberinto_arbol(laberinto, [pos[0], pos[1] + 1]))

    # izquierda
    if pos[0] > 0 and pos[1] - 1 > 0:
        if laberinto[pos[0]][pos[1] - 1] == '0' or laberinto[pos[0]][pos[1] - 1] == 'x' or laberinto[pos[0]][pos[1] - 1] == 'y':
            print("If izquierda")
            return Nodo(laberinto[pos[0]][pos[1]], laberinto_arbol(laberinto, [pos[0], pos[1] - 1]))


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
        return True
    except ValueError:
        pass
    return False

# print(busqueda_matriz([[1,9,3],[4,5,6],[7,8,9]],3,9))
m = [['1', '1', '1'], ['0', 'x', 'y'], ['1', '0', '1']]

print(laberinto_arbol(m, busqueda_matriz(m, 3, 'x'),[]))
