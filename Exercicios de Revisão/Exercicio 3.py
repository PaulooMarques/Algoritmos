# 3. Estatísticas de Notas
# Leia as notas de uma turma e:
# • Calcule a média;
# • Mostre a maior e a menor nota;
# • Exiba o percentual de alunos acima da média.


def calcular_estatisticas():

    print("=== ESTATÍSTICAS DE NOTAS ===")

    notas = []

    while True:
        entrada = input("Digite uma nota (ou 'fim' para encerrar): ")

        if entrada.lower() == "fim":
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota deve estar entre 0 e 10!")
        except ValueError:
            print("Digite um número válido!")

    if not notas:
        print("Nenhuma nota foi inserida!")
        return

    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)

    acima_media = sum(1 for nota in notas if nota > media)
    percentual = (acima_media / len(notas)) * 100

    print("\n" + "=" * 40)
    print("RESULTADOS:")
    print("=" * 40)
    print(f"Total de notas: {len(notas)}")
    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior_nota:.1f}")
    print(f"Menor nota: {menor_nota:.1f}")
    print(f"Alunos acima da média: {acima_media} ({percentual:.1f}%)")

    print(f"\nNotas inseridas: {[f'{n:.1f}' for n in notas]}")


if __name__ == "__main__":
    calcular_estatisticas()
