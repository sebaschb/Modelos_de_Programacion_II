class Nodo:
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def __str__(self):
        return "v:{}(l:{},r:{})".format(self.valor,self.izq,self.der)

def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if arbol.valor > valor:
        return buscar(arbol.izq, valor)
    return buscar(arbol.der, valor)

def a_lista(arbol):
    if arbol == None:
        return []
    return a_lista(arbol.izq) + [arbol.valor] + a_lista(arbol.der)

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



arbol = Nodo(25, Nodo(18,Nodo(10),Nodo(20)),Nodo(50,Nodo(40)))

print(insertar_nodo(arbol,21).izq.der.der.valor)
print(insertar_nodo(arbol,12))
print(lista_arbol([9,8,5,1,7,11,10]))
print(lista_arbol([7,4,5,6,2,3,1]))