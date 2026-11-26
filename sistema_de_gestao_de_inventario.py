# Sistema de Gestão de Inventário

#Percorrer todos os produtos utilizando for.
#Numerar os produtos usando enumerate(), começando em 1.
#Apresentar nome, preço e quantidade de cada produto.
#Calcular o valor total de cada produto em stock (preço × quantidade).
#Calcular o valor financeiro total do inventário.
#Contar quantos produtos têm stock inferior a 5 unidades.
#Contar quantos produtos têm stock de 5 ou mais unidades.
#Identificar o produto mais caro.
#Apresentar um relatório final.

print("\n================== SISTEMA DE GESTÃO DE INVENTÁRIO ==================")

print("\n========================= LISTA DE PRODUTOS =========================\n")

produtos = [
    ["Teclado", 12500, 8],
    ["Rato", 5000, 15],
    ["Monitor", 95000, 4],
    ["Impressora", 65000, 6],
    ["Colunas", 15000, 10],
    ["Webcam", 35000, 3]
]

valor_total_financeiro_do_inventario = 0
quantidade_stock_inferior_5 = 0
quantidade_stock_igual_ou_superior_5 = 0
produto_mais_caro = 0

total_produtos = len(produtos)

for indice, produto in enumerate(produtos, start=1):

    nome = produto[0]
    preco = produto[1]
    quantidade_stock = produto[2]
    valor = preco * quantidade_stock

    print(f"{indice} - {nome} | Preço: {preco:,} Kz | Stock: {quantidade_stock} | Valor: {valor:,} Kz ")

    if quantidade_stock < 5:
        quantidade_stock_inferior_5 += 1

    else:
        quantidade_stock_igual_ou_superior_5 += 1

    if preco > produto_mais_caro:
        produto_mais_caro = preco
        nome_mais_caro = nome

    valor_total_financeiro_do_inventario += valor

print("\n================== RELATÓRIO INVENTÁRIO ==================\n")
print(f"Total de produtos: {total_produtos}")
print(f"Produtos com stock inferior a 5: {quantidade_stock_inferior_5}")
print(f"Produtos com stock igual ou superior a 5: {quantidade_stock_igual_ou_superior_5}")
print(f"\nValor financeiro total do inventário: {valor_total_financeiro_do_inventario:,} Kz")
print(f"Produto mais caro: {nome_mais_caro} | {produto_mais_caro:,} Kz")
print("\n==========================================================")
