# Problema 2 – Academia e Desempenho dos Atletas
# A academia guarda os atletas em uma lista de dicionários, cada um com:
# nome, idade, modalidades (lista de esportes), treinos (dicionário com o nome do esporte como
# chave e a quantidade de treinos realizados como valor).
# Tarefas:
# 1. Crie uma função que calcule a média de idade dos atletas que praticam um esporte
# específico.
# 2. Crie uma função que, dado um atleta, informe qual esporte ele mais treinou.
# 3. Monte uma lista com os atletas que praticam mais de 2 modalidades e exiba seus
# nomes.
atletas = [
    {
        "nome": "Rafael",
        "idade": 28,
        "modalidades": ["Futebol", "Natação"],
        "treinos": {"Futebol": 25, "Natação": 15},
    },
    {
        "nome": "Amanda",
        "idade": 24,
        "modalidades": ["Volei", "Basquete", "Tenis"],
        "treinos": {"Volei": 18, "Basquete": 12, "Tenis": 8},
    },
    {
        "nome": "Gabriel",
        "idade": 31,
        "modalidades": ["Futebol", "Handebol"],
        "treinos": {"Futebol": 30, "Handebol": 22},
    },
    {
        "nome": "Larissa",
        "idade": 19,
        "modalidades": ["Ginastica", "Danca", "Atletismo"],
        "treinos": {"Ginastica": 35, "Danca": 28, "Atletismo": 14},
    },
]


def media_idade_esporte():

    esportes_disponiveis = set()
    for atleta in atletas:
        for modalidade in atleta["modalidades"]:
            esportes_disponiveis.add(modalidade)

    print("Esportes disponíveis:")
    for esporte in sorted(esportes_disponiveis):
        print(f"- {esporte}")
    print()

    esporte_escolhido = input("Digite o nome do esporte: ")

    idades = []
    for atleta in atletas:
        if esporte_escolhido in atleta["modalidades"]:
            idades.append(atleta["idade"])

    if len(idades) > 0:
        media = sum(idades) / len(idades)
        return media
    else:
        return 0


def esporte_mais_treinado():

    print("Atletas disponíveis:")
    for atleta in atletas:
        print(f"- {atleta['nome']}")
    print()

    nome_atleta = input("Digite o nome do atleta: ")

    for atleta in atletas:
        if atleta["nome"] == nome_atleta:
            esporte_max = ""
            treinos_max = 0

            for esporte, quantidade in atleta["treinos"].items():
                if quantidade > treinos_max:
                    treinos_max = quantidade
                    esporte_max = esporte

            return esporte_max

    return "Atleta não encontrado"


resultado_media = media_idade_esporte()
print(f"Média de idade: {resultado_media:.1f} anos")
print()


esporte_favorito = esporte_mais_treinado()
print(f"Esporte mais treinado: {esporte_favorito}")
print()

atletas_versateis = []

for atleta in atletas:
    if len(atleta["modalidades"]) > 2:
        atletas_versateis.append(atleta["nome"])

if len(atletas_versateis) > 0:
    print("Atletas que praticam mais de 2 modalidades:")
    for nome in atletas_versateis:
        print(f"- {nome}")
else:
    print("Nenhum atleta pratica mais de 2 modalidades.")
