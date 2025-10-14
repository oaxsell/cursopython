"""
Algoritmo 181- Criar um algoritmo que imprima todos os números de 1 até 100 e a
soma deles
"""
soma = 0
for numero in range(1,101):
    soma += numero
    print(f"{numero}")

# Exibir a soma total
print(f"A soma de todos os números de 1 a 100 é {soma}")