# 9. Planejamento de Exercícios
# Contexto: Uma academia planeja 3 tipos de exercícios para 4 alunos diferentes.
# Tarefa: Crie uma matriz 4x3 que registre quantas repetições cada aluno deve fazer e calcule o
# total de repetições de cada exercício.

repeticoes = [
    [15, 20, 12],
    [25, 30, 20],
    [20, 25, 15],
    [30, 35, 25]
]

alunos = ["João", "Maria", "Carlos", "Ana"]
exercicios = ["Flexões", "Abdominais", "Agachamentos"]
niveis = ["Iniciante", "Intermediário", "Intermediário", "Avançado"]

print("=" * 70)
print("ACADEMIA FIT - PLANEJAMENTO DE TREINO")
print("=" * 70)

print("\nPlano de repetições por aluno:\n")
print(f"{'Aluno':<12} {'Nível':<15} {'Flexões':<12} {'Abdominais':<12} {'Agachamentos'}")
print("-" * 70)

for i in range(len(repeticoes)):
    print(f"{alunos[i]:<12} {niveis[i]:<15} {repeticoes[i][0]:<12} {repeticoes[i][1]:<12} {repeticoes[i][2]}")

print("\n" + "=" * 70)
print("TOTAL DE REPETIÇÕES POR ALUNO")
print("=" * 70)

totais_alunos = []
for i in range(len(repeticoes)):
    total = sum(repeticoes[i])
    totais_alunos.append(total)
    print(f"{alunos[i]} ({niveis[i]}): {total} repetições totais")

print("\n" + "=" * 70)
print("TOTAL DE REPETIÇÕES POR EXERCÍCIO")
print("=" * 70)

totais_exercicios = []
for exercicio in range(3):
    total_exercicio = 0
    for aluno in range(len(repeticoes)):
        total_exercicio += repeticoes[aluno][exercicio]
    totais_exercicios.append(total_exercicio)
    print(f"{exercicios[exercicio]}: {total_exercicio} repetições (todos os alunos)")

print("\n" + "=" * 70)
print("MÉDIA DE REPETIÇÕES POR EXERCÍCIO")
print("=" * 70)

for i in range(len(exercicios)):
    media = totais_exercicios[i] / len(repeticoes)
    print(f"{exercicios[i]}: {media:.1f} repetições por aluno")

print("\n" + "=" * 70)
print("ANÁLISE DE DESEMPENHO")
print("=" * 70)

aluno_destaque = totais_alunos.index(max(totais_alunos))
print(f"Aluno mais dedicado: {alunos[aluno_destaque]} ({totais_alunos[aluno_destaque]} repetições)")

exercicio_intenso = totais_exercicios.index(max(totais_exercicios))
print(f"Exercício mais praticado: {exercicios[exercicio_intenso]} ({totais_exercicios[exercicio_intenso]} repetições)")

exercicio_leve = totais_exercicios.index(min(totais_exercicios))
print(f"Exercício menos praticado: {exercicios[exercicio_leve]} ({totais_exercicios[exercicio_leve]} repetições)")

print("\n" + "=" * 70)
print("DETALHAMENTO INDIVIDUAL")
print("=" * 70)

for i in range(len(alunos)):
    print(f"\n{alunos[i]} - Nível: {niveis[i]}")
    print("-" * 40)
    
    melhor_exercicio = repeticoes[i].index(max(repeticoes[i]))
    pior_exercicio = repeticoes[i].index(min(repeticoes[i]))
    
    print(f"  Ponto forte: {exercicios[melhor_exercicio]} ({repeticoes[i][melhor_exercicio]} reps)")
    print(f"  Para melhorar: {exercicios[pior_exercicio]} ({repeticoes[i][pior_exercicio]} reps)")
    print(f"  Total semanal: {totais_alunos[i]} repetições")

print("\n" + "=" * 70)
print("ESTIMATIVA DE CALORIAS QUEIMADAS")
print("=" * 70)

calorias_por_rep = [0.35, 0.20, 0.40]

print("\nCalorias estimadas por aluno:")
for i in range(len(alunos)):
    calorias_total = 0
    for j in range(len(exercicios)):
        calorias_total += repeticoes[i][j] * calorias_por_rep[j]
    print(f"{alunos[i]}: {calorias_total:.1f} kcal")

total_geral = sum(totais_alunos)
print("\n" + "=" * 70)
print(f"TOTAL DE REPETIÇÕES DA TURMA: {total_geral} repetições")
print("=" * 70)