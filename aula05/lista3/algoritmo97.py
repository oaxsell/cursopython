"""
Algoritmo 97 - Entrar comum número e informar se ele é divisível por 10, por 5,
por 2 ou se não é divisível por nenhum destes..
"""
# ENTRADA DE DADOS
numero = int(input("Digite um número inteiro: "))

# CONDIÇÃO E SAÍDA DE DADOS
if numero % 10 == 0 and numero % 5 == 0 and numero % 2 == 0:
    print(f"O número {numero} é divisível por 10, 5 ou 2.")
else:
    print(f"O número {numero} não é divisível por 10, 5 ou 2.")