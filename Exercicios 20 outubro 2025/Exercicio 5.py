# 5. Registro de Pontos em Jogos
# Contexto: Uma liga de esportes registra pontos de 3 times em 4 jogos.
# Tarefa: Crie uma matriz 3x4 com os pontos e determine qual time teve maior pontuação total.

pontos = [
    [85, 92, 78, 88],
    [90, 87, 95, 91],
    [82, 79, 84, 80]
]

times = ["Águias", "Leões", "Tigres"]

print("=" * 70)
print("LIGA DE BASQUETE - REGISTRO DE PONTOS")
print("=" * 70)

print("\nPontuação por jogo:")
print("\nTime\t\tJogo 1\tJogo 2\tJogo 3\tJogo 4")
print("-" * 70)

for i in range(len(pontos)):
    print(f"{times[i]}\t\t{pontos[i][0]}\t{pontos[i][1]}\t{pontos[i][2]}\t{pontos[i][3]}")

print("\n" + "=" * 70)
print("PONTUAÇÃO TOTAL POR TIME")
print("=" * 70)

totais_times = []
for i in range(len(pontos)):
    total = sum(pontos[i])
    totais_times.append(total)
    media = total / len(pontos[i])
    print(f"{times[i]}: {total} pontos (Média: {media:.1f} pontos/jogo)")

print("\n" + "=" * 70)
print("CLASSIFICAÇÃO FINAL")
print("=" * 70)

classificacao = []
for i in range(len(times)):
    classificacao.append([times[i], totais_times[i]])

classificacao.sort(key=lambda x: x[1], reverse=True)

for posicao, (time, total) in enumerate(classificacao, 1):
    if posicao == 1:
        print(f"{posicao}º lugar: {time} - {total} pontos CAMPEÃO!")
    elif posicao == 2:
        print(f"{posicao}º lugar: {time} - {total} pontos ")
    else:
        print(f"{posicao}º lugar: {time} - {total} pontos ")

print("\n" + "=" * 70)
print("ESTATÍSTICAS DOS JOGOS")
print("=" * 70)

for jogo in range(4):
    print(f"\nJogo {jogo + 1}:")
    pontos_jogo = []
    for time in range(len(pontos)):
        pontos_jogo.append(pontos[time][jogo])
    
    maior_pontuacao = max(pontos_jogo)
    time_destaque = times[pontos_jogo.index(maior_pontuacao)]
    
    print(f"  Melhor time: {time_destaque} ({maior_pontuacao} pontos)")
    print(f"  Média de pontos: {sum(pontos_jogo) / len(pontos_jogo):.1f}")

print("\n" + "=" * 70)
print("ANÁLISE DE DESEMPENHO")
print("=" * 70)

for i in range(len(pontos)):
    melhor_jogo = max(pontos[i])
    pior_jogo = min(pontos[i])
    jogo_melhor = pontos[i].index(melhor_jogo) + 1
    jogo_pior = pontos[i].index(pior_jogo) + 1
    
    print(f"\n{times[i]}:")
    print(f"  Melhor desempenho: Jogo {jogo_melhor} ({melhor_jogo} pontos)")
    print(f"  Pior desempenho: Jogo {jogo_pior} ({pior_jogo} pontos)")
    print(f"  Variação: {melhor_jogo - pior_jogo} pontos")

print("=" * 70)