# Enunciado – Jogo Campo Minado em Python
# Objetivo
# Desenvolver um jogo simples de Campo Minado (Minesweeper) em Python, utilizando
# matrizes (listas bidimensionais) e funções para organizar o código.
# Descrição do Problema
# Você deverá implementar uma versão simplificada do Campo Minado em modo texto.
# O tabuleiro é representado por uma matriz, onde algumas posições contêm minas e as demais
# são espaços seguros.
# O jogador deve escolher coordenadas (linha e coluna) e tentar abrir as posições sem explodir
# uma mina.
# Regras do Jogo
# 1. O jogo começa com um tabuleiro oculto (exemplo: 5x5).
# 2. As minas são distribuídas aleatoriamente no tabuleiro.
# 3. O jogador escolhe posições digitando linha e coluna.
# 4. Se o jogador abrir:
# o Uma célula sem mina, ela mostra quantas minas há nas 8 posições vizinhas.
# o Uma célula com mina, o jogo termina ( Game Over).
# 5. O jogo termina quando:
# o O jogador abre todas as células seguras ( Vitória), ou
# o Explode uma mina ( Derrota).
# Requisitos Técnicos
# • O tabuleiro deve ser representado por uma matriz (lista de listas).
# • Devem ser usadas funções para modularizar o código, por exemplo:
# o criar_tabuleiro(linhas, colunas, qtd_minas)
# o mostrar_tabuleiro(tabuleiro, revelado)
# o contar_minas_vizinhas(tabuleiro, linha, coluna)
# o jogar(tabuleiro)
# • Use o módulo random para posicionar minas aleatoriamente.
# • Utilize try/except para tratar erros de entrada (ex: coordenadas inválidas).
# • O jogador deve ver o progresso a cada jogada.

import random

def criar_tabuleiro(linhas, colunas, qtd_minas):
    tabuleiro = [["~" for _ in range(colunas)] for _ in range(linhas)]
    minas_locais = []
    
    while len(minas_locais) < qtd_minas:
        i = random.randint(0, linhas - 1)
        j = random.randint(0, colunas - 1)
        if [i, j] not in minas_locais:
            minas_locais.append([i, j])
    return tabuleiro, minas_locais

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for index, coluna in enumerate(linha):
            print(f"{coluna}  ", end=" ")
            if index == len(linha) - 1:
                print("")

def contar_minas_vizinhas(linha, coluna, minas_locais, linhas, colunas):
    qtd_minas_vizinhas = 0
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if 0 <= i < linhas and 0 <= j < colunas and [i, j] in minas_locais:
                qtd_minas_vizinhas += 1
    return qtd_minas_vizinhas

def atualizar_mapa(tabuleiro, marcador, linha, coluna):
    tabuleiro[linha][coluna] = marcador

def jogar(tabuleiro, minas_locais):
    casas_seguras = len(tabuleiro) * len(tabuleiro[0]) - len(minas_locais)
    casas_seguras_descobertas = 0
    casas_jogadas = []

    print("=== CAMPO MINADO ===")
    print(f"Total de minas: {len(minas_locais)}")

    while True:
        print(f"\nCasas descobertas: {casas_seguras_descobertas}/{casas_seguras}")
        print("=== Tabuleiro ===\n")
        mostrar_tabuleiro(tabuleiro)

        linha_input = input("Digite uma linha (0-4): ")
        coluna_input = input("Digite uma coluna (0-4): ")

        try:
            linha_input = int(linha_input)
            coluna_input = int(coluna_input)
            if linha_input not in range(len(tabuleiro)) or coluna_input not in range(len(tabuleiro)):
                raise ValueError
        except ValueError:
            print("Valores inválidos! Tente novamente.")
            continue

        if [linha_input, coluna_input] in casas_jogadas:
            print("Esta casa já foi descoberta! Tente novamente.")
            continue

        if [linha_input, coluna_input] in minas_locais:
            print("Você explodiu em uma mina!")
            atualizar_mapa(tabuleiro, "X", linha_input, coluna_input)
            mostrar_tabuleiro(tabuleiro)
            print("Game Over!")
            break

        minas_vizinhas = contar_minas_vizinhas(linha_input, coluna_input, minas_locais, len(tabuleiro), len(tabuleiro[0]))
        print(f"Há {minas_vizinhas} mina(s) por perto! ({linha_input}, {coluna_input})")

        atualizar_mapa(tabuleiro, minas_vizinhas, linha_input, coluna_input)
        casas_seguras_descobertas += 1
        casas_jogadas.append([linha_input, coluna_input])

        if casas_seguras_descobertas >= casas_seguras:
            print("PARABÉNS! Você descobriu todas as casas sem minas!")
            mostrar_tabuleiro(tabuleiro)
            break

tabuleiro, minas_locais = criar_tabuleiro(5, 5, 10)
jogar(tabuleiro, minas_locais)
