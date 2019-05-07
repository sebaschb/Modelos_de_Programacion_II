from divisible import divisible


def divisibles(n):
    return [x for x in range(1, n+1) if divisible(n, x)]
