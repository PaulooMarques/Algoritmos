# 10. Registro de Chuva
# Contexto: Uma estação meteorológica registra chuva em 7 dias, para 3 cidades.
# Tarefa: Crie uma matriz 3x7 com os valores de chuva (mm) e determine qual cidade teve mais
# chuva na semana.

chuva = [
    [12.5, 0.0, 8.3, 15.7, 22.0, 5.2, 0.0],
    [5.8, 3.2, 0.0, 10.5, 18.3, 25.0, 12.7],
    [0.0, 0.0, 2.5, 5.0, 8.5, 15.0, 20.5]
]

cidades = ["Rio de Janeiro", "São Paulo", "Belo Horizonte"]
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

print("=" * 90)
print("ESTAÇÃO METEOROLÓGICA - REGISTRO SEMANAL DE CHUVA")
print("=" * 90)

print("\nRegistro de precipitação (mm):\n")
print(f"{'Cidade':<18}", end="")
for dia in dias:
    print(f"{dia:>10}", end="")
print()
print("-" * 90)

for i in range(len(chuva)):
    print(f"{cidades[i]:<18}", end="")
    for j in range(len(chuva[i])):
        if chuva[i][j] == 0.0:
            print(f"{'---':>10}", end="")
        else:
            print(f"{chuva[i][j]:>10.1f}", end="")
    print()

print("\n" + "=" * 90)
print("ACUMULADO SEMANAL POR CIDADE")
print("=" * 90)

totais_cidades = []
for i in range(len(chuva)):
    total = sum(chuva[i])
    totais_cidades.append(total)
    
    if total >= 80:
        classificacao = "Volume ALTO"
    elif total >= 40:
        classificacao = "Volume MODERADO"
    else:
        classificacao = "Volume BAIXO"
    
    print(f"{cidades[i]:<20}: {total:>6.1f} mm - {classificacao}")

print("\n" + "=" * 90)
print("RANKING DE PRECIPITAÇÃO")
print("=" * 90)

ranking = []
for i in range(len(cidades)):
    ranking.append([cidades[i], totais_cidades[i]])

ranking.sort(key=lambda x: x[1], reverse=True)

for posicao, (cidade, total) in enumerate(ranking, 1):
    if posicao == 1:
        print(f"{posicao}º lugar: {cidade} - {total:.1f} mm (Mais chuvosa)")
    elif posicao == 2:
        print(f"{posicao}º lugar: {cidade} - {total:.1f} mm ")
    else:
        print(f"{posicao}º lugar: {cidade} - {total:.1f} mm (Menos chuvosa)")

print("\n" + "=" * 90)
print("PRECIPITAÇÃO MÉDIA DIÁRIA (TODAS AS CIDADES)")
print("=" * 90)

totais_dias = []
for dia in range(7):
    total_dia = 0
    for cidade in range(len(chuva)):
        total_dia += chuva[cidade][dia]
    media_dia = total_dia / len(chuva)
    totais_dias.append(total_dia)
    
    status = ""
    if total_dia == 0:
        status = "Sem chuva"
    elif total_dia < 10:
        status = "Chuva fraca"
    elif total_dia < 30:
        status = "Chuva moderada"
    else:
        status = "Chuva forte"
    
    print(f"{dias[dia]:<12}: Total {total_dia:>5.1f} mm | Média {media_dia:>5.1f} mm - {status}")

print("\n" + "=" * 90)
print("ANÁLISE DETALHADA POR CIDADE")
print("=" * 90)

for i in range(len(cidades)):
    print(f"\n{cidades[i]}:")
    print("-" * 50)
    
    dias_com_chuva = sum(1 for valor in chuva[i] if valor > 0)
    dias_sem_chuva = 7 - dias_com_chuva
    
    maior_chuva = max(chuva[i])
    dia_maior = chuva[i].index(maior_chuva)
    
    chuvas_registradas = [valor for valor in chuva[i] if valor > 0]
    media_dias_chuva = sum(chuvas_registradas) / len(chuvas_registradas) if chuvas_registradas else 0
    
    print(f"  • Dias com chuva: {dias_com_chuva}")
    print(f"  • Dias sem chuva: {dias_sem_chuva}")
    print(f"  • Maior precipitação: {maior_chuva:.1f} mm ({dias[dia_maior]})")
    print(f"  • Média (dias chuvosos): {media_dias_chuva:.1f} mm")
    print(f"  • Acumulado semanal: {totais_cidades[i]:.1f} mm")

print("\n" + "=" * 90)
print("ESTATÍSTICAS GERAIS DA SEMANA")
print("=" * 90)

dia_mais_chuvoso = totais_dias.index(max(totais_dias))
print(f"Dia mais chuvoso: {dias[dia_mais_chuvoso]} ({totais_dias[dia_mais_chuvoso]:.1f} mm total)")

dia_mais_seco = totais_dias.index(min(totais_dias))
print(f"Dia mais seco: {dias[dia_mais_seco]} ({totais_dias[dia_mais_seco]:.1f} mm total)")

total_geral = sum(totais_cidades)
media_geral = total_geral / len(cidades)
print(f"\nPrecipitação total (todas as cidades): {total_geral:.1f} mm")
print(f"Média por cidade: {media_geral:.1f} mm")

print("=" * 90)