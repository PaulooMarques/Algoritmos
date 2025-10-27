# Problema 4 – Ranking de Filmes
# Você recebeu uma lista de filmes (cada filme é um dicionário) com os campos:
# • titulo → nome do filme
# • diretor → nome do diretor
# • bilheteria → valor em milhões de dólares
# • avaliacoes → lista de notas de 1 a 10
# Tarefas:
# 1. Top 3 maiores bilheterias
# o Crie uma função top_bilheteria(filmes) que retorne os 3 filmes com maior
# bilheteria.
# 2. Top 3 melhores avaliados
# o Crie uma função top_avaliacao(filmes) que calcule a média das avaliações de
# cada filme e retorne os 3 melhores.
# 3. Bilheteria por diretor
# o Crie uma função bilheteria_por_diretor(filmes) que retorne um dicionário onde a
# chave é o diretor e o valor é o total de bilheteria de todos os seus filmes.
# 4. Campeão absoluto
# o Crie uma função campeao(filmes) que mostre qual filme é a melhor combinação
# de bilheteria alta e avaliação média alta.

filmes = [
    {
        "titulo": "Pulp Fiction",
        "diretor": "Quentin Tarantino",
        "bilheteria": 214.2,
        "avaliacoes": [9, 8, 10, 9, 8, 7, 9, 10],
    },
    {
        "titulo": "Forrest Gump",
        "diretor": "Robert Zemeckis",
        "bilheteria": 677.9,
        "avaliacoes": [10, 9, 8, 9, 10, 8, 9],
    },
    {
        "titulo": "The Godfather",
        "diretor": "Francis Ford Coppola",
        "bilheteria": 134.9,
        "avaliacoes": [10, 10, 9, 10, 9, 10, 8, 9],
    },
    {
        "titulo": "Titanic",
        "diretor": "James Cameron",
        "bilheteria": 2194.4,
        "avaliacoes": [8, 7, 9, 8, 6, 7, 8, 9],
    },
    {
        "titulo": "Avatar",
        "diretor": "James Cameron",
        "bilheteria": 2923.7,
        "avaliacoes": [7, 8, 9, 8, 7, 9, 8],
    },
    {
        "titulo": "Goodfellas",
        "diretor": "Martin Scorsese",
        "bilheteria": 46.8,
        "avaliacoes": [9, 10, 9, 8, 9, 10, 9, 8],
    },
]


def top_bilheteria(filmes_lista):

    filmes_ordenados = []
    for filme in filmes_lista:
        filmes_ordenados.append(filme)

    for i in range(len(filmes_ordenados)):
        for j in range(i + 1, len(filmes_ordenados)):
            if filmes_ordenados[i]["bilheteria"] < filmes_ordenados[j]["bilheteria"]:
                filmes_ordenados[i], filmes_ordenados[j] = (
                    filmes_ordenados[j],
                    filmes_ordenados[i],
                )

    return filmes_ordenados[:3]


def top_avaliacao(filmes_lista):

    filmes_com_media = []

    for filme in filmes_lista:
        avaliacoes = filme["avaliacoes"]
        if len(avaliacoes) > 0:
            media = sum(avaliacoes) / len(avaliacoes)
        else:
            media = 0

        filme_com_media = {
            "titulo": filme["titulo"],
            "diretor": filme["diretor"],
            "bilheteria": filme["bilheteria"],
            "media_avaliacoes": media,
        }
        filmes_com_media.append(filme_com_media)

    for i in range(len(filmes_com_media)):
        for j in range(i + 1, len(filmes_com_media)):
            if (
                filmes_com_media[i]["media_avaliacoes"]
                < filmes_com_media[j]["media_avaliacoes"]
            ):
                filmes_com_media[i], filmes_com_media[j] = (
                    filmes_com_media[j],
                    filmes_com_media[i],
                )

    return filmes_com_media[:3]


def bilheteria_por_diretor(filmes_lista):

    total_por_diretor = {}

    for filme in filmes_lista:
        diretor = filme["diretor"]
        bilheteria = filme["bilheteria"]

        if diretor in total_por_diretor:
            total_por_diretor[diretor] += bilheteria
        else:
            total_por_diretor[diretor] = bilheteria

    return total_por_diretor


def campeao(filmes_lista):

    melhor_filme = ""
    melhor_score = 0

    for filme in filmes_lista:

        avaliacoes = filme["avaliacoes"]
        if len(avaliacoes) > 0:
            media_avaliacao = sum(avaliacoes) / len(avaliacoes)
        else:
            media_avaliacao = 0

        bilheteria_normalizada = filme["bilheteria"] / 1000
        score = bilheteria_normalizada * media_avaliacao

        if score > melhor_score:
            melhor_score = score
            melhor_filme = filme["titulo"]

    return melhor_filme


print("=== ANÁLISE DE FILMES ===")
print()


print("1. TOP 3 MAIORES BILHETERIAS:")
top3_bilheteria = top_bilheteria(filmes)
for i, filme in enumerate(top3_bilheteria, 1):
    print(f"{i}º lugar: {filme['titulo']} - ${filme['bilheteria']} milhões")
print()


print("2. TOP 3 MELHORES AVALIADOS:")
top3_avaliacao = top_avaliacao(filmes)
for i, filme in enumerate(top3_avaliacao, 1):
    print(f"{i}º lugar: {filme['titulo']} - Média: {filme['media_avaliacoes']:.2f}")
print()


print("3. BILHETERIA POR DIRETOR:")
bilheteria_diretores = bilheteria_por_diretor(filmes)
for diretor, total in bilheteria_diretores.items():
    print(f"{diretor}: ${total:.1f} milhões")
print()


print("4. CAMPEÃO ABSOLUTO:")
filme_campeao = campeao(filmes)
print(f"Melhor combinação de bilheteria e avaliação: {filme_campeao}")
