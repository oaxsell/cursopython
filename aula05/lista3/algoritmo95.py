"""
Algoritmo 95 - Entrar com um número e informar se ele é ou não divisível por 5.
"""
# ENTRADA DE DADOS
numero = int(input("Digite um número inteiro: "))

# CONDIÇÃO E SAÍDA DE DADOS
if numero % 5 == 0:
    print(f"O número {numero} é divisível por 5.")
else:
    print(f"O número {numero} não é divisível por 5.")