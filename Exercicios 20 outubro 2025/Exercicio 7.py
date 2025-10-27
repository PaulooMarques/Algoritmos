# 7. Vendas Semanais
# Contexto: Uma cafeteria registra vendas de 5 produtos durante 7 dias.
# Tarefa: Armazene os valores em uma matriz 5x7 e calcule a receita total semanal de cada
# produto.

vendas = [
    [150.50, 180.00, 165.75, 190.00, 220.50, 310.00, 280.25],
    [85.00, 95.50, 88.00, 92.75, 105.00, 145.50, 130.00],
    [120.00, 135.50, 128.00, 142.00, 155.75, 198.00, 175.50],
    [65.50, 72.00, 68.50, 75.00, 82.50, 110.00, 95.00],
    [45.00, 52.50, 48.00, 55.00, 62.00, 88.00, 75.50]
]

produtos = ["Café Expresso", "Cappuccino", "Pão de Queijo", "Bolo de Cenoura", "Croissant"]
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

print("=" * 90)
print("CAFETERIA BOM SABOR - RELATÓRIO DE VENDAS SEMANAL")
print("=" * 90)

print("\nVendas diárias (R$):\n")
print(f"{'Produto':<18}", end="")
for dia in dias:
    print(f"{dia:>10}", end="")
print()
print("-" * 90)

for i in range(len(vendas)):
    print(f"{produtos[i]:<18}", end="")
    for j in range(len(vendas[i])):
        print(f"{vendas[i][j]:>10.2f}", end="")
    print()

print("\n" + "=" * 90)
print("RECEITA TOTAL SEMANAL POR PRODUTO")
print("=" * 90)

totais_produtos = []
for i in range(len(vendas)):
    total = sum(vendas[i])
    totais_produtos.append(total)
    print(f"{produtos[i]:<20}: R$ {total:>8.2f}")

print("\n" + "=" * 90)
print("RECEITA TOTAL POR DIA DA SEMANA")
print("=" * 90)

totais_dias = []
for dia in range(7):
    total_dia = 0
    for produto in range(len(vendas)):
        total_dia += vendas[produto][dia]
    totais_dias.append(total_dia)
    print(f"{dias[dia]:<12}: R$ {total_dia:>8.2f}")

print("\n" + "=" * 90)
print("ANÁLISE DE DESEMPENHO")
print("=" * 90)

produto_mais_vendido = totais_produtos.index(max(totais_produtos))
print(f"Produto mais vendido: {produtos[produto_mais_vendido]} (R$ {totais_produtos[produto_mais_vendido]:.2f})")

produto_menos_vendido = totais_produtos.index(min(totais_produtos))
print(f"Produto menos vendido: {produtos[produto_menos_vendido]} (R$ {totais_produtos[produto_menos_vendido]:.2f})")

melhor_dia = totais_dias.index(max(totais_dias))
print(f"\nMelhor dia de vendas: {dias[melhor_dia]} (R$ {totais_dias[melhor_dia]:.2f})")

pior_dia = totais_dias.index(min(totais_dias))
print(f"Dia com menor faturamento: {dias[pior_dia]} (R$ {totais_dias[pior_dia]:.2f})")

receita_total_semana = sum(totais_produtos)
print(f"\nRECEITA TOTAL DA SEMANA: R$ {receita_total_semana:.2f}")

media_diaria = receita_total_semana / 7
print(f"Média de faturamento diário: R$ {media_diaria:.2f}")

print("\n" + "=" * 90)
print("PARTICIPAÇÃO DE CADA PRODUTO NA RECEITA TOTAL")
print("=" * 90)

for i in range(len(produtos)):
    percentual = (totais_produtos[i] / receita_total_semana) * 100
    barra = "█" * int(percentual / 2) 
    print(f"{produtos[i]:<20}: {percentual:>5.1f}% {barra}")

print("=" * 90)