def invertir(lista):
    print("entra")
    if len(lista)==0:
        return []
    else:
        return invertir(lista[1:])+[lista[0],]

print(invertir([4,-2,1,4,-10]))
