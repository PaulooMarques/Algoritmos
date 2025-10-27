# Nível 2 – Aplicações Práticas
# 6. Busca de Nome em Lista
# o Peça ao usuário para digitar nomes e depois procure um nome específico usando
# busca linear.
# 7. Busca Binária Recursiva
# o Implemente a versão recursiva da busca binária em uma lista ordenada.
# 8. Comparar Tempo de Execução
# o Compare o tempo de execução da busca linear e busca binária em uma lista
# com 1 milhão de elementos. Use o módulo time.
# 9. Encontrar Primeira Ocorrência (Busca Binária Modificada)
# o Dada uma lista ordenada com elementos repetidos, use busca binária modificada
# para encontrar o índice da primeira ocorrência de um número.
# 10. Localizar Intervalo de Índices
# • Encontre o intervalo (início e fim) de um número que aparece mais de uma vez usando
# busca binária (ex: [1,2,2,2,3,4] > número 2 > índices 1 a 3).

import random
import time

def busca_nome(nomes, nome_procurado):
    for i, nome in enumerate(nomes):
        if nome.lower() == nome_procurado.lower():
            return i
    return None

def busca_binaria_recursiva(lista, alvo, esq=0, dir=None):
    if dir is None:
        dir = len(lista) - 1
    
    if esq > dir:
        return None
    
    meio = (esq + dir) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, dir)
    else:
        return busca_binaria_recursiva(lista, alvo, esq, meio - 1)

def busca_primeira_ocorrencia(lista, alvo):
    esq, dir = 0, len(lista) - 1
    resultado = None
    
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            resultado = meio
            dir = meio - 1
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return resultado

def encontrar_intervalo(lista, alvo):
    primeira = busca_primeira_ocorrencia(lista, alvo)
    if primeira is None:
        return None
    
    esq, dir = 0, len(lista) - 1
    ultima = None
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            ultima = meio
            esq = meio + 1
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    
    return (primeira, ultima)

print("="*60)
print("EXERCÍCIO 2 - APLICAÇÕES PRÁTICAS")
print("="*60)

print("\n6. BUSCA DE NOME")
nomes = []
print("Digite nomes (enter vazio para parar):")
while True:
    nome = input(f"  Nome {len(nomes)+1}: ").strip()
    if not nome:
        break
    nomes.append(nome)

if nomes:
    print(f"\nLista: {nomes}")
    while True:
        buscar = input("Nome para buscar: ").strip()
        if buscar:
            idx = busca_nome(nomes, buscar)
            print(f"Resultado: {'Índice ' + str(idx) if idx is not None else 'Não encontrado'}")
            break
        print("Nome não pode estar vazio!")

print("\n7. BUSCA BINÁRIA RECURSIVA")
lista = sorted([random.randint(1, 100) for _ in range(15)])  # ORDENAR lista
print(f"Lista ordenada: {lista}")
while True:
    try:
        numero = int(input("Número para buscar: "))
        
        inicio = time.time()
        idx = busca_binaria_recursiva(lista, numero)
        tempo = time.time() - inicio
        
        print(f"Resultado: {'Índice ' + str(idx) if idx is not None else 'Não encontrado'}")
        print(f"Tempo: {tempo:.6f}s")
        break
    except ValueError:
        print("Digite um número válido!")
        continue

print("\n8. COMPARAÇÃO DE TEMPO (1 milhão de elementos)")
tamanho = 1000000

lista_des = [random.randint(1, tamanho*10) for _ in range(tamanho)]
lista_ord = sorted(lista_des)

alvo = lista_ord[tamanho // 2]

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return None

inicio = time.time()
busca_linear(lista_des, alvo)
t_linear = time.time() - inicio

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

inicio = time.time()
busca_binaria(lista_ord, alvo)
t_binaria = time.time() - inicio

print(f"Linear:  {t_linear:.6f}s")
print(f"Binária: {t_binaria:.6f}s")
print(f"Speedup: {t_linear/t_binaria:.0f}x")

print("\n9. PRIMEIRA OCORRÊNCIA")
lista9 = None
while lista9 is None:
    try:
        entrada = input("Digite números separados por espaço: ").strip()
        if entrada:
            lista9 = sorted([int(x) for x in entrada.split()])  # ORDENAR lista
            print(f"Lista ordenada: {lista9}")
        else:
            print("Digite pelo menos um número!")
            continue
    except ValueError:
        print("Digite apenas números válidos!")
        continue

while True:
    try:
        numero = int(input("Buscar primeira ocorrência de: "))
        
        inicio = time.time()
        idx = busca_primeira_ocorrencia(lista9, numero)
        tempo = time.time() - inicio
        
        print(f"Resultado: {'Índice ' + str(idx) if idx is not None else 'Não encontrado'}")
        print(f"Tempo: {tempo:.6f}s")
        break
    except ValueError:
        print("Digite um número válido!")
        continue

print("\n10. INTERVALO DE ÍNDICES")
lista10 = None
while lista10 is None:
    try:
        entrada = input("Digite números separados por espaço: ").strip()
        if entrada:
            lista10 = sorted([int(x) for x in entrada.split()])  # ORDENAR lista
            print(f"Lista ordenada: {lista10}")
        else:
            print("Digite pelo menos um número!")
            continue
    except ValueError:
        print("Digite apenas números válidos!")
        continue

while True:
    try:
        numero = int(input("Buscar intervalo de: "))

        inicio = time.time()
        intervalo = encontrar_intervalo(lista10, numero)
        tempo = time.time() - inicio
        
        if intervalo:
            print(f"Intervalo: [{intervalo[0]}, {intervalo[1]}] ({intervalo[1]-intervalo[0]+1} ocorrências)")
        else:
            print("Não encontrado")
        print(f"Tempo: {tempo:.6f}s")
        break
    except ValueError:
        print("Digite um número válido!")
        continue

print("\n" + "="*60)