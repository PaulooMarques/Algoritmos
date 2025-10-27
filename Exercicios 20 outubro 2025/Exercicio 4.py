# 4. Controle de Estoque
# Contexto: Uma loja possui 4 produtos e verifica o estoque em 3 lojas diferentes.
# Tarefa: Crie uma matriz 4x3 com as quantidades de cada produto em cada loja e calcule o total
# de cada produto.

estoque = [
    [45, 32, 28],
    [120, 85, 95],
    [67, 54, 71],
    [33, 41, 29]
]

produtos = ["Notebook", "Mouse", "Teclado", "Webcam"]
lojas = ["Loja Centro", "Loja Shopping", "Loja Bairro"]

print("=" * 70)
print("CONTROLE DE ESTOQUE - REDE DE LOJAS")
print("=" * 70)

print("\nEstoque atual:")
print("\nProduto\t\t\tLoja Centro\tLoja Shopping\tLoja Bairro")
print("-" * 70)

for i in range(len(estoque)):
    print(f"{produtos[i]:<20}\t{estoque[i][0]}\t\t{estoque[i][1]}\t\t{estoque[i][2]}")

print("\n" + "=" * 70)
print("TOTAL DE CADA PRODUTO (TODAS AS LOJAS)")
print("=" * 70)

totais_produtos = []
for i in range(len(estoque)):
    total = sum(estoque[i])
    totais_produtos.append(total)
    print(f"{produtos[i]}: {total} unidades")

print("\n" + "=" * 70)
print("TOTAL DE PRODUTOS POR LOJA")
print("=" * 70)

for loja in range(3):
    total_loja = 0
    for produto in range(len(estoque)):
        total_loja += estoque[produto][loja]
    print(f"{lojas[loja]}: {total_loja} unidades")

print("\n" + "=" * 70)
print("ANÁLISE DO ESTOQUE")
print("=" * 70)

produto_maior_estoque = totais_produtos.index(max(totais_produtos))
print(f"Produto com maior estoque: {produtos[produto_maior_estoque]} ({totais_produtos[produto_maior_estoque]} unidades)")

produto_menor_estoque = totais_produtos.index(min(totais_produtos))
print(f"Produto com menor estoque: {produtos[produto_menor_estoque]} ({totais_produtos[produto_menor_estoque]} unidades)")

estoque_total_geral = sum(totais_produtos)
print(f"\nEstoque total geral: {estoque_total_geral} unidades")

print("\n" + "=" * 70)
print("ALERTAS DE ESTOQUE BAIXO (< 35 unidades)")
print("=" * 70)

tem_alerta = False
for i in range(len(estoque)):
    for j in range(len(estoque[i])):
        if estoque[i][j] < 35:
            tem_alerta = True
            print(f"• {produtos[i]} na {lojas[j]}: {estoque[i][j]} unidades")

if not tem_alerta:
    print("✓ Todos os produtos estão com estoque adequado!")

print("=" * 70)