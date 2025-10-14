"""
Algoritmo 96 - Entrar com um número e informar se ele é divisível por 3 e por 7.
"""
# ENTRADA DE DADOS
numero = int(input("Digite um número inteiro: "))

# CONDIÇÃO E SAÍDA DE DADOS
if numero % 3 == 0 and numero % 7 == 0:
    print(f"O número {numero} é divisível por 3 e 7.")
else:
    print(f"O número {numero} não é divisível por 3 e 7.")