import math
def obtener_matriz():
    return [x.split() for x in open("matriz6x6.txt").readlines()]

print(obtener_matriz())

"""
 funcion que recorre una fila o columna especifica de una matriz, paritiendo de un inicio y un fin,
 ademas se especifica en que sentido recorrer
 
 parametros:
    ini (int): indica inicio del recorrido de la fila o columna de la matriz
    fin (int): entero que indica el fin del recorrido de la fila o columna de la matriz
    col (int): fila o columna a recorrer
    inver (boolean): modo de recorrido de la fila o columna, ejem: izq a der, o der a iz 
    pos (String): determina si se recorre una fila o una columna('V')
    matriz (list[list]: matriz que se va a recorrer
"""

def matriz_0():
    return len(obtener_matriz()[0])

def recorrer(ini, fin, col, inver, pos, matriz):
    #tamMatriz = len(matriz[0])
    if fin-ini <= 0:
        return 0
    else:
        if pos == 'V':
            vertical(matriz_0(), fin, col, inver, matriz)
        else:
            horizontal(matriz_0(), fin, col, inver, matriz)

        recorrer(ini, fin-1, col, inver, pos, matriz)


"""
 funcion auxiliar que ayuda a "recorrer" de manera horizontal

 parametros:
    tamMatriz (int): tamaño de la matriz
    fin (int): entero que indica el fin del recorrido de la fila o columna de la matriz
    col (int): fila o columna a recorrer
    inver (boolean): modo de recorrido de la fila o columna, ejem: izq a der, o der a iz   
    matriz (list[list]: matriz que se va a recorrer
"""
def horizontal(tamMatriz,fin, col, inver, matriz):
    if inver:
        print(matriz[col][fin - 1])
    else:
        print(matriz[col][tamMatriz - fin])


"""
 funcion auxiliar que ayuda a "recorrer" de manera vertical

 parametros:
    tamMatriz (int): tamaño de la matriz
    fin (int): entero que indica el fin del recorrido de la fila o columna de la matriz
    col (int): fila o columna a recorrer
    inver (boolean): modo de recorrido de la fila o columna, ejem: izq a der, o der a iz   
    matriz (list[list]: matriz que se va a recorrer
"""
def vertical(tamMatriz,fin, col, inver, matriz):
    if inver:
        print(matriz[fin - 1][col])
    else:
        print(matriz[tamMatriz - fin][col])


"""
 funcion que hace un recorrido en espiral de una matriz cuadrada, funcion recursiva
 que recorre en cada iteracion el borde una matriz cada vez mas pequeña y centrada

 parametros:
    tam (int): tamaño de la matriz
    p (list[list]: matriz cuadrada que se va a recorrer
"""
def tam_matriz():
    return len(obtener_matriz())

def recorridoEspiral(tam, p):
    #tamano = len(p)
    if tam < 1:
        return 0
    else:
        # recorre borde superior matriz de izq a der
        recorrer(tam_matriz()-tam, tam, tam_matriz()-tam, False, 'H', p)

        # recorre borde derecho matriz de arriba a abajo,
        # quitando en el recorrido el primer elemento, puesto que ya se habia tendio en cuenta en el anterior paso
        recorrer(tam_matriz()-tam, tam-1, tam-1, False, 'V', p)

        # recorre borde superior matriz de der a iz
        # quitando en el recorrido el primer elemento, puesto que ya se habia tendio en cuenta en el anterior paso
        recorrer(tam_matriz()-tam, tam-1, tam-1, True, 'H', p)

        # recorre borde derecho matriz de abajo a arriba
        # quitando en el recorrido el primer y ultimo elemento, puesto que ya se habia tendio en cuenta en los pasos anteriores
        recorrer(tam_matriz()-tam+1, tam-1, tam_matriz()-tam, True, 'V', p)

        # nueva iteracion, recorrido interno matriz de tam-1
        recorridoEspiral(tam-1, p)


#recorrer(0, len(p), 0, False, 'H', p)
#print("----")
#recorrer(0, len(p)-1, len(p)-1, False, 'V', p)
#print("----")
#recorrer(0, len(p)-1, len(p)-1, True, 'H', p)
#print("----")
#recorrer(1, len(p)-1, 0, True, 'V', p)


recorridoEspiral(len(obtener_matriz()), obtener_matriz())
