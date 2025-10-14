"""
Algoritmo 184 – Entrar com 8 números e , para cada número, imprimir o logaritmo
desse número na base 10.
"""
import math
for i in range(1,9):
    numero = float(input("Digite um número: "))
    log_numero = math.log10(numero)
    print(f"O log de {numero} é {log_numero}")
