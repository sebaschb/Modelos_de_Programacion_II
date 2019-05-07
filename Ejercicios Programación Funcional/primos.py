from esPrimo import esPrimo

def primos(n):
    return [x for x in range(1, n+1) if esPrimo(x)]

print(primos(100))