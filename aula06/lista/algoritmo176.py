"""
Algoritmo 176 – Imprimir os 100 primeiros pares
"""
contador = 0
for numero in range(1,202):
    if numero % 2 == 0 and contador < 100:
        contador += 1
        print(f"[{contador}] = {numero}")
    