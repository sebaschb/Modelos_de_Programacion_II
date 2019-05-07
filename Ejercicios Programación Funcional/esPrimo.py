from divisibles import divisibles


def esPrimo(p):
    return len(divisibles(p)) <= 2
