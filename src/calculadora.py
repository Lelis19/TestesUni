def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Não é possível fazer divisão por zero!"
    return n1 / n2

def potencia(n1, n2):
    return n1 ** n2