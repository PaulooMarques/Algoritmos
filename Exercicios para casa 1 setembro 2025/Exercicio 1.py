# Caso 4: Análise de Vendas Mensais


vendas_diarias = [10, 15, 20, 5, 0, 8, 12, 18, 25, 7, 14, 22, 16, 9, 13, 11, 19, 24, 6, 17, 21, 3, 26, 15, 8, 12, 29, 4, 18, 23]

print("=== ANÁLISE DE VENDAS MENSAIS ===")


total_vendas = sum(vendas_diarias)
print(f"1. Total de vendas: {total_vendas}")


max_vendas = max(vendas_diarias)
min_vendas = min(vendas_diarias)
dia_max = vendas_diarias.index(max_vendas) + 1
dia_min = vendas_diarias.index(min_vendas) + 1

print(f"2. Maior venda: Dia {dia_max} ({max_vendas})")
print(f"   Menor venda: Dia {dia_min} ({min_vendas})")


media_vendas = total_vendas / len(vendas_diarias)
print(f"3. Média diária: {media_vendas:.2f}")


dias_acima_media = [(i+1, v) for i, v in enumerate(vendas_diarias) if v > media_vendas]
print(f"4. Dias acima da média: {len(dias_acima_media)} dias")
for dia, vendas in dias_acima_media:
    print(f"   Dia {dia}: {vendas} vendas")