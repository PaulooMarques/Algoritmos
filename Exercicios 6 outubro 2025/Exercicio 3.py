# Nível 3 – Desafios
# 11. Busca em Lista de Dicionários
# • Dada uma lista de dicionários representando pessoas ({"nome": "Ana", "idade":
# 25}), implemente uma busca linear para encontrar a pessoa com nome "João".
# 12. Jogo: Adivinhe o Número (Busca Binária)
# • O computador escolhe um número entre 1 e 100. O jogador tenta adivinhar, e o
# computador responde se é maior ou menor. Use lógica de busca binária para resolver
# com o menor número de tentativas.
# 13. Buscar Produtos por Preço
# • Dada uma lista de produtos com preços, implemente uma busca para encontrar todos os
# produtos com um determinado preço.
# 14. Implementar sua própria função index()
# • Crie uma função meu_index(lista, valor) que funcione como o método
# list.index(), usando busca sequencial.

import random

def buscar_pessoa(pessoas, nome):
    for pessoa in pessoas:
        if pessoa.get("nome", "").lower() == nome.lower():
            return pessoa
    return None


def jogo_computador_adivinha(limite_min, limite_max):
    print(f"\nPense em um número entre {limite_min} e {limite_max}")
    input("Pressionei ENTER quando estiver pronto...")

    esq, dir = limite_min, limite_max
    tentativas = 0

    while esq <= dir:
        tentativas += 1
        palpite = (esq + dir) // 2

        print(f"\nTentativa {tentativas}: Meu palpite é {palpite}")
        print("  1 - Meu número é MENOR")
        print("  2 - Acertouu!")
        print("  3 - Meu número é MAIOR")

        while True:
            try:
                resposta = int(input("Sua resposta: "))
                if resposta in [1, 2, 3]:
                    break
                print("Digite 1, 2 ou 3!")
            except ValueError:
                print("Digite um número válido!")
                continue

        if resposta == 2:
            print(f"\n Acertei em {tentativas} tentativas usando busca binária!")
            return tentativas
        elif resposta == 1:
            dir = palpite - 1
        else:
            esq = palpite + 1

    print("\nAlgo deu errado... você pensou em um número válido?")
    return tentativas


def buscar_produtos_preco(produtos, preco):
    return [p for p in produtos if abs(p["preco"] - preco) < 0.01]


def meu_index(lista, valor):
    for i, item in enumerate(lista):
        if item == valor:
            return i
    raise ValueError(f"{valor} is not in list")


print("=" * 60)
print("EXERCÍCIO 3 - DESAFIOS")
print("=" * 60)

print("\n11. BUSCA EM LISTA DE DICIONÁRIOS")
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 30},
    {"nome": "Maria", "idade": 28},
]

print("Base de dados:")
for p in pessoas:
    print(f"  - {p['nome']}, {p['idade']} anos")

while True:
    nome = input("\nDigite o nome para buscar: ").strip()
    if nome:
        resultado = buscar_pessoa(pessoas, nome)
        if resultado:
            print(f"Encontrado: {resultado}")
        else:
            print(f"'{nome}' não encontrado")
        break
    print("Nome não pode estar vazio!")

print("\n12. JOGO: ADIVINHE O NÚMERO")
print("O computador vai adivinhar o número que você pensar!")

while True:
    try:
        limite_min = int(input("Limite mínimo: "))
        limite_max = int(input("Limite máximo: "))
        if limite_max > limite_min:
            break
        print("O máximo deve ser maior que o mínimo!")
    except ValueError:
        print("Digite números válidos!")
        continue

jogo_computador_adivinha(limite_min, limite_max)

print("\n13. BUSCAR PRODUTOS POR PREÇO")
produtos = [
    {"nome": "Notebook", "preco": 3000.00},
    {"nome": "Mouse", "preco": 50.00},
    {"nome": "Teclado", "preco": 150.00},
    {"nome": "Webcam", "preco": 150.00},
    {"nome": "Monitor", "preco": 1000.00},
]

print("\nProdutos disponíveis:")
for p in produtos:
    print(f"  - {p['nome']}: R$ {p['preco']:.2f}")

while True:
    try:
        preco = float(input("\nBuscar produtos com preço R$: "))
        encontrados = buscar_produtos_preco(produtos, preco)
        print(f"\n{len(encontrados)} produto(s) encontrado(s):")
        for p in encontrados:
            print(f"  - {p['nome']} (R$ {p['preco']:.2f})")
        if len(encontrados) == 0:
            print("  (Nenhum produto com esse preço)")
        break
    except ValueError:
        print("Digite um preço válido!")
        continue


print("\n14. IMPLEMENTAR FUNÇÃO index()")
lista = [10, 20, 30, 40, 50, 30, 60]
print(f"Lista: {lista}")

while True:
    try:
        valor = int(input("Valor para buscar: "))

        try:
            idx_custom = meu_index(lista, valor)
            idx_nativo = lista.index(valor)

            print(f"\nmeu_index(lista, {valor}) = {idx_custom}")
            print(f"list.index(lista, {valor}) = {idx_nativo}")

            if idx_custom == idx_nativo:
                print("Função funcionando corretamente!")
            else:
                print("Resultado diferente!")
        except ValueError as e:
            print(f"\n{e}")
        break
    except ValueError:
        print("Digite um número válido!")
        continue
