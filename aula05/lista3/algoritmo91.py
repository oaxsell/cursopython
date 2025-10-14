"""
Algoritmo 91 – Construir um algoritmo que leia dois valores numéricos inteiros e
efetue a adição; caso o resultado seja maior que 10, apresentá-lo.
"""
# ENTRADA DE DADOS
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# CÁLCULO
soma = num1 + num2

# CONDIÇÃO E SAÍDA DE DADOS
if soma > 10:
    print(f"A soma dos números {num1} e {num2} é: {soma}")
