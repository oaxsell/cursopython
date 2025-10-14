"""
Algoritmo 183- Entrar com 10 números e imprimir o quadrado de cada número
"""
import math
for i in range(1,11):
    numero = float(input("Digite um número: "))
    quadrado_numero = pow(numero, 2)
    print(f"O quadrado de {numero} é {quadrado_numero}")
