"""
Algoritmo 43 – Entrar com um número e imprimir o logaritmo desse número na
base 10.
"""
import math
# ENTRADA DE DADOS
numero = float(input("Digite um número: "))

# CÁLCULO
logaritmo_base_10 = math.log10(numero)

# SAÍDA DE DADOS
print(f"O logaritmo na base 10 de {numero} é: {logaritmo_base_10}")