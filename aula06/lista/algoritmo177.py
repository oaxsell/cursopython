"""
Algoritmo 177 - Imprimir os múltiplos de 5, no intervalo de 1 até 500
"""
contador = 0
for numero in range(1,501):
    if numero % 5 == 0:
        contador += 1
        print(f"[{contador}] = {numero}")
    