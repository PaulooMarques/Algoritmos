# Caso4: Análise de Vendas Mensais
# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:
# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.


def analisar_vendas_mensais(vendas):

    total_vendas = sum(vendas)

    max_vendas = max(vendas)
    min_vendas = min(vendas)
    dia_max = vendas.index(max_vendas) + 1
    dia_min = vendas.index(min_vendas) + 1

    media_vendas = total_vendas / len(vendas)

    dias_acima_media = []
    for i in range(len(vendas)):
        if vendas[i] > media_vendas:
            dias_acima_media.append(i + 1)

    return {
        "total": total_vendas,
        "dia_max": dia_max,
        "vendas_max": max_vendas,
        "dia_min": dia_min,
        "vendas_min": min_vendas,
        "media": round(media_vendas, 2),
        "dias_acima_media": dias_acima_media,
    }


def exibir_resultado(vendas, resultado):
    print(f"Vendas diárias: {vendas}")
    print("-" * 50)
    print(f"1. Total de vendas no mês: {resultado['total']}")
    print(
        f"2. Dia com MAIS vendas: Dia {resultado['dia_max']} ({resultado['vendas_max']} vendas)"
    )
    print(
        f"   Dia com MENOS vendas: Dia {resultado['dia_min']} ({resultado['vendas_min']} vendas)"
    )
    print(f"3. Média de vendas por dia: {resultado['media']}")
    print(f"4. Dias acima da média: {resultado['dias_acima_media']}")
    print("-" * 50)


if __name__ == "__main__":

    print("Digite as vendas separadas por vírgula (ex: 10,15,20,5):")
    try:
        entrada = input("Vendas: ")
        vendas_usuario = [int(x.strip()) for x in entrada.split(",")]
        resultado3 = analisar_vendas_mensais(vendas_usuario)
        exibir_resultado(vendas_usuario, resultado3)
    except:
        print("Formato inválido ou entrada cancelada.")
