class Nodo:
    def __int__(self, valor, hijos=[]):
        self.valor = valor
        self.hijos =hijos


def busqueda_matriz(lista,tam,valor):
    if lista == []:
        return []
    else:
        try:
            return [tam-len(lista),lista[0].index(valor)]
        except ValueError:
            pass
        return busqueda_matriz(lista[1:],tam,valor)

def laberinto_arbol(laberinto,pos):


    

    # abajo
    if laberinto[pos[0]+1][pos[1]] == '0' or laberinto[pos[0]+1][pos[1]] =='x' or laberinto[pos[0]+1][pos[1]] =='y':
        return Nodo(laberinto[pos[0]][pos[1]],laberinto_arbol(laberinto,[pos[0]+1,pos[1]]))

    #arriba
    if laberinto[pos[0] - 1][pos[1]] == '0' or laberinto[pos[0] - 1][pos[1]] == 'x' or laberinto[pos[0] - 1][pos[1]] == 'y':
        return Nodo(laberinto[pos[0]][pos[1]],laberinto_arbol(laberinto, [pos[0] - 1, pos[1]]))

    # derecha
    if laberinto[pos[0]][pos[1]+1] == '0' or laberinto[pos[0]][pos[1]+1] == 'x' or laberinto[pos[0]][pos[1]+1] == 'y':
        return Nodo(laberinto[pos[0]][pos[1]],laberinto_arbol(laberinto, [pos[0] , pos[1]+1]))

    # izquierda
    if laberinto[pos[0]][pos[1] - 1] == '0' or laberinto[pos[0]][pos[1] - 1] == 'x' or laberinto[pos[0]][pos[1] - 1] == 'y':
        return Nodo(laberinto[pos[0]][pos[1]],laberinto_arbol(laberinto, [pos[0], pos[1] - 1]))

    if laberinto[pos[0]][pos[1]] == '1':
        return Nodo(None)


#print(busqueda_matriz([[1,9,3],[4,5,6],[7,8,9]],3,9))
m=[['0','0','x'],['1','0','0'],['1','0','y']]

print(laberinto_arbol(m,busqueda_matriz(m,3,'x')))