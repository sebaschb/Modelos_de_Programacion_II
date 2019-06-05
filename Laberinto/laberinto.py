class Nodo:
    def __init__(self, valor,hijos=[]):
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

visitados = []

def recorrido(laberinto, pos):
    hijos = []
    if pos not in visitados:
        visitados.append(pos)
        if laberinto[pos[0]-1][pos[1]] != '1':
            posL = [pos[0]-1, pos[1]]
            hijos.append(recorrido(laberinto, posL))
        if laberinto[pos[0]+1][pos[1]] != '1':
            posR = [pos[0]+1, pos[1]]
            hijos.append(recorrido(laberinto, posR))
        if laberinto[pos[0]][pos[1]+1] != '1':
            posU = [pos[0], pos[1]+1]
            hijos.append(recorrido(laberinto, posU))
        if laberinto[pos[0]][pos[1]-1] != '1':
            posD = [pos[0], pos[1]-1]
            hijos.append(recorrido(laberinto, posD))
        return Nodo(laberinto[pos[0]][pos[1]], hijos)
    else:
        return Nodo(laberinto[pos[0]][pos[1]])

def buscar_valor(arbol, valor):
    if arbol.valor == valor:
        return True
    else:
        if arbol.hijos == []:
            return False
        else:
            return buscar_valor(arbol.hijos[0], valor) or buscar_valor_hijos(arbol.hijos[1:], valor)

def buscar_valor_hijos(lista, valor):
    if lista == []:
        return False
    else:
        return buscar_valor(lista[0], valor) or buscar_valor_hijos(lista[1:], valor)

def esSolucionable(arbol):
    estado = False
    for hijo in arbol.hijos:
        estado = estado or buscar_valor(hijo,'y')
    if estado:
        print("es solucionable")
    else:
        print("no es solucionable")

def imprimir(arbol):
    if arbol.hijos == []:
        print(arbol.valor)
    else:
        for hijo in arbol.hijos:
            imprimir(hijo)

laberinto = [list(linea[:-1]) for linea in open("laberinto.txt").readlines()]

arbol=recorrido(laberinto, busqueda_matriz(laberinto, len(laberinto), 'x'))

esSolucionable(arbol)

