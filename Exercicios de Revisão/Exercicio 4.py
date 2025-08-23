# 4. Busca Linear
# Dada uma lista de nomes, implemente uma função que busque um nome digitado pelo usuário.
# Informe a posição em que ele aparece ou diga que não foi encontrado.


def busca_linear(lista_nomes, nome_procurado):

    for i in range(len(lista_nomes)):
        if lista_nomes[i].lower() == nome_procurado.lower():
            return i
    return -1


def sistema_busca():

    print("=== BUSCA DE NOMES ===")

    nomes = []

    print("Digite os nomes da lista (digite 'fim' para encerrar):")
    while True:
        nome = input("Nome: ").strip()
        if nome.lower() == "fim":
            break
        if nome:
            nomes.append(nome)

    if not nomes:
        print("Nenhum nome foi inserido!")
        return

    print(f"\nLista criada: {nomes}")
    print(f"Total de nomes: {len(nomes)}")

    # Sistema de busca
    while True:
        print("\n" + "-" * 30)
        nome_busca = input("Digite o nome para buscar (ou 'sair'): ").strip()

        if nome_busca.lower() == "sair":
            print("Encerrando busca.")
            break

        if not nome_busca:
            print("Digite um nome válido!")
            continue

        # Realizar busca
        posicao = busca_linear(nomes, nome_busca)

        if posicao != -1:
            print(f"✓ Nome '{nome_busca}' encontrado na posição {posicao}")
        else:
            print(f"✗ Nome '{nome_busca}' não foi encontrado na lista")


if __name__ == "__main__":
    sistema_busca()
