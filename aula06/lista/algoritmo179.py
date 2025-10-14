"""
Algoritmo 179- Criar um algoritmo que imprima os números pares no intervalo de
1 a 600.
"""
contador = 0
for numero in range(1,601):
    if numero % 2 == 0:
        contador += 1
        print(f"[{contador}] = {numero}")