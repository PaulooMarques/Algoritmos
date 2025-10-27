# Nível 1 – Fundamentos
# 1. Busca Linear Simples
# o Dado um vetor de números inteiros e um número alvo, use busca sequencial para
# verificar se o número está presente.
# o Extra: informe o índice se encontrar.
# 2. Contar Ocorrências (Busca Linear)
# o Conte quantas vezes um número aparece na lista usando busca sequencial.
# 3. Maior Número (Busca Linear)
# o Use busca sequencial para encontrar o maior número em uma lista.
# 4. Menor Número (Busca Linear)
# o Similar ao anterior, mas encontre o menor valor.
# 5. Verificar Elemento (Busca Binária)
# o Dada uma lista ordenada, implemente a busca binária para verificar se o
# elemento existe.

import random
import time
import sys

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return None

def contar_ocorrencias(lista, alvo):
    return sum(1 for num in lista if num == alvo)

def encontrar_maior(lista):
    maior = lista[0]
    for num in lista[1:]:
        if num > maior:
            maior = num
    return maior

def encontrar_menor(lista):
    menor = lista[0]
    for num in lista[1:]:
        if num < menor:
            menor = num
    return menor

def busca_binaria(lista, alvo):
    esq, dir = 0, len(lista) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return None

print("="*60)
print("EXERCÍCIO 1 - FUNDAMENTOS")
print("="*60)

lista = [15, 3, 8, 22, 3, 45, 8, 12, 3, 67, 8, 34]
print(f"\nLista de teste: {lista}")

numero = int(input("\n1. Digite um número para buscar: "))
idx = busca_linear(lista, numero)
print(f"   Resultado: {'Encontrado no índice ' + str(idx) if idx is not None else 'Não encontrado'}")

numero = int(input("\n2. Digite um número para contar ocorrências: "))
count = contar_ocorrencias(lista, numero)
print(f"   Aparece {count} vez(es)")

print(f"\n3. Maior número: {encontrar_maior(lista)}")

print(f"\n4. Menor número: {encontrar_menor(lista)}")

lista_ord = sorted(lista)  
print(f"\n5. Lista ordenada: {lista_ord}")
numero = int(input("   Digite um número para busca binária: "))
idx = busca_binaria(lista_ord, numero)
print(f"   Resultado: {'Encontrado no índice ' + str(idx) if idx is not None else 'Não encontrado'}")

print("\n" + "="*60)
print("COMPARAÇÃO DE DESEMPENHO - 1.000.000 ELEMENTOS")
print("="*60)

tamanho = 1000000
print("\nGerando listas...")
lista_grande = [random.randint(1, tamanho * 10) for _ in range(tamanho)]
lista_ord_grande = sorted(lista_grande)  

alvo_meio = lista_ord_grande[tamanho // 2]
alvo_fim = lista_ord_grande[-1]

print("\nBUSCA LINEAR:")
inicio = time.time()
busca_linear(lista_grande, alvo_meio)
t_linear_meio = time.time() - inicio

inicio = time.time()
busca_linear(lista_grande, alvo_fim)
t_linear_fim = time.time() - inicio

print(f"  Meio: {t_linear_meio:.6f}s")
print(f"  Fim:  {t_linear_fim:.6f}s")

print("\nBUSCA BINÁRIA:")
inicio = time.time()
busca_binaria(lista_ord_grande, alvo_meio)
t_binaria_meio = time.time() - inicio

inicio = time.time()
busca_binaria(lista_ord_grande, alvo_fim)
t_binaria_fim = time.time() - inicio

print(f"  Meio: {t_binaria_meio:.6f}s")
print(f"  Fim:  {t_binaria_fim:.6f}s")

print(f"\nSPEEDUP:")
print(f"  Meio: {t_linear_meio/t_binaria_meio:.0f}x mais rápido")
print(f"  Fim:  {t_linear_fim/t_binaria_fim:.0f}x mais rápido")

print(f"\nMEMÓRIA:")
mem_des = sys.getsizeof(lista_grande) / (1024*1024)
mem_ord = sys.getsizeof(lista_ord_grande) / (1024*1024)
print(f"  Lista desordenada: {mem_des:.2f} MB")
print(f"  Lista ordenada:    {mem_ord:.2f} MB")

print("\n" + "="*60)