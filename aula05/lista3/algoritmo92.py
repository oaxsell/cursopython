"""
Algoritmo 92- Construir um algoritmo que leia dois números e efetue a adição.
Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se
a ele mais 8; Caso o valor somado seja menor ou igual a 20, este deverá ser
apresentado subtraindo-se 5.
"""
# ENTRADA DE DADOS
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# CÁLCULO
soma = num1 + num2

# CONDIÇÃO E SAÍDA DE DADOS
if soma > 20:
    resultado = soma + 8
    print(f"O resultado da soma {soma} é maior que 20. Somando 8, temos: {resultado}")
else:
    resultado = soma - 5
    print(f"O resultado da soma {soma} é menor ou igual a 20. Subtraindo 5, temos: {resultado}")