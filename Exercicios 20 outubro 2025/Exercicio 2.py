# 2. Grade de Notas de Alunos
# Contexto: Uma turma de 4 alunos realizou 3 provas.
# Tarefa: Armazene as notas em uma matriz 4x3 e calcule a média de cada aluno e a média de
# cada prova.

notas = [
    [8.5, 7.0, 9.2],   
    [6.8, 7.5, 7.2],  
    [9.0, 8.5, 9.5],   
    [5.5, 6.0, 7.0]  
]

nomes_alunos = ["Ana", "Bruno", "Carla", "Daniel"]

print("\nNotas dos alunos:")
print("\nAluno\t\tProva 1\tProva 2\tProva 3")
print("-" * 60)

for i in range(len(notas)):
    print(f"{nomes_alunos[i]}\t\t{notas[i][0]}\t{notas[i][1]}\t{notas[i][2]}")

print("\n" + "=" * 60)
print("MÉDIA DE CADA ALUNO")
print("=" * 60)

medias_alunos = []
for i in range(len(notas)):
    soma = sum(notas[i])
    media = soma / len(notas[i])
    medias_alunos.append(media)
    
    situacao = "Aprovado ✓" if media >= 7.0 else "Reprovado ✗"
    print(f"{nomes_alunos[i]}: {media:.2f} - {situacao}")

print("\n" + "=" * 60)
print("MÉDIA DE CADA PROVA")
print("=" * 60)

for prova in range(3): 
    soma_prova = 0
    for aluno in range(len(notas)):
        soma_prova += notas[aluno][prova]
    
    media_prova = soma_prova / len(notas)
    print(f"Prova {prova + 1}: {media_prova:.2f}")


print("\n" + "=" * 60)
print("ESTATÍSTICAS GERAIS")
print("=" * 60)

melhor_aluno = medias_alunos.index(max(medias_alunos))
pior_aluno = medias_alunos.index(min(medias_alunos))

print(f"Melhor desempenho: {nomes_alunos[melhor_aluno]} ({medias_alunos[melhor_aluno]:.2f})")
print(f"Precisa de reforço: {nomes_alunos[pior_aluno]} ({medias_alunos[pior_aluno]:.2f})")
print(f"Média geral da turma: {sum(medias_alunos) / len(medias_alunos):.2f}")
print("=" * 60)