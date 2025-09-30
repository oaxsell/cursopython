"""
Cadastrar um produto e descobrir o valor total
"""
# string [e] texto
nome_do_produto = input("Digite o nome do produto: ")
qtd_de_produto = int(input("Digite a quantidade do produto: "))
valor_do_produto = float(input("Digite o valor do produto: "))
valor_total = qtd_de_produto * valor_do_produto
print(
    f"O produto {nome_do_produto} com valor unitario de R$ {valor_do_produto} "
    f"e quantidade de {qtd_de_produto} tem o valor total de R$ {valor_total}"
)

# Estrutura Condicional
# Se o valor total for maior que 1000, aplicar 10% de desconto
if valor_total >= 1000:
    valor_total = valor_total * 0.9  # Aplica o desconto de 10%
    print("Desconto de 10% aplicado")
    print(f"O valor com desconto é R$ {valor_total}")
else:
    print("Sem desconto")
    print(f"O valor total é R$ {valor_total}")