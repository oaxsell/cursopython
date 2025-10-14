"""
Algoritmo 93 - Entrar com um número e imprimir a raiz quadrada do número caso
ele seja positivo e o quadrado do número caso ele seja negativo.
"""
import math

# ENTRADA DE DADOS
numero = float(input("Digite um número: "))

# CONDIÇÃO E SAÍDA DE DADOS
if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")
else:
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é: {quadrado}")