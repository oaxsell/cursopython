import math

# Definição das dimensões do campo de futebol em metros
largura_campo_futebol_metros = 60
comprimento_campo_futebol_metros = 100

# Calculo da área do campo de futebol em km quadrados
# 1 km = 1000 m, aplicando a conversão para km²
# 60 m = 0.06 km
# 100 m = 0.1 km
# Área = largura * comprimento
area_campo_futebol_km2 = ( ( largura_campo_futebol_metros / 1000 ) * ( comprimento_campo_futebol_metros / 1000 ) )
print(f"Área do campo de futebol: {area_campo_futebol_km2} km²")

# Área prevista para devastação da Amazônia em km quadrados
area_devastacao_amazonia_km2 = float(input("Digite a área prevista para devastação da Amazônia em km²: "))

# Cálculo do número de campos de futebol que cabem na área de devastação
numero_campos_futebol = area_devastacao_amazonia_km2 / area_campo_futebol_km2

# Quantos campos de futebol é a previsão da ONG WWF Brasil para devastação da Amazônia?
# Arredondando para o número inteiro mais próximo
numero_campos_futebol_arredondado = round(numero_campos_futebol)
# Exibindo o resultado
print(f"Na área prevista para devastação da Amazônia cabem aproximadamente {numero_campos_futebol_arredondado:,.0f} campos de futebol.")