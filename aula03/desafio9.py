# calculadora do estatistico
def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero"
def potencia(a,b):
    return a ** b