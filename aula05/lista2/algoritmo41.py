"""
Algoritmo 41 – Entrar com quatro números e imprimir a média ponderada ,
sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.
"""
# PESOS DAS MEDIAS
PESO_1 = 1
PESO_2 = 2
PESO_3 = 3
PESO_4 = 4
some_dos_pesos = PESO_1 + PESO_2 + PESO_3 + PESO_4

# ENTRADA DE DADOS
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
terceiro_numero = float(input("Digite o terceiro número: "))
quarto_numero = float(input("Digite o quarto número: "))

media_ponderada = (((primeiro_numero * PESO_1) + (segundo_numero * PESO_2) + (terceiro_numero * PESO_3) + (quarto_numero * PESO_4)) / (some_dos_pesos))

print(f"A média ponderada é: {media_ponderada}")
