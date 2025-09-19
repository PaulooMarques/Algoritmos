# Problema 1 – Restaurante Inteligente
# Um restaurante armazena os pedidos do dia em uma lista de dicionários, onde cada pedido tem:
# cliente, itens (lista de dicionários com prato e preco).
# Tarefas:
# 1. Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando
# todos os itens pedidos).
# 2. Crie uma função que descubra qual prato foi o mais vendido no dia.
# 3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente.

pedidos = [
    {
        "cliente": "Fernanda",
        "itens": [
            {"prato": "Salmão Grelhado", "preco": 45},
            {"prato": "Água Mineral", "preco": 4},
            {"prato": "Tiramisu", "preco": 18},
        ],
    },
    {
        "cliente": "Carlos",
        "itens": [
            {"prato": "Risotto", "preco": 38},
            {"prato": "Vinho Tinto", "preco": 22},
        ],
    },
    {
        "cliente": "Isabella",
        "itens": [
            {"prato": "Risotto", "preco": 38},
            {"prato": "Salada", "preco": 15},
            {"prato": "Café Expresso", "preco": 6},
            {"prato": "Petit Gateau", "preco": 20},
        ],
    },
    {
        "cliente": "Roberto",
        "itens": [
            {"prato": "Picanha na Chapa", "preco": 52},
            {"prato": "Caipirinha", "preco": 12},
        ],
    },
]


def valor_total_gasto():

    print("Clientes de Hoje:")
    for pedido in pedidos:
        print(f"- {pedido['cliente']}")
    print()

    nome_cliente = input("Digite o nome do cliente: ")

    for pedido in pedidos:
        if pedido["cliente"] == nome_cliente:
            total = 0
            for item in pedido["itens"]:
                total += item["preco"]
            return total
    return 0


def prato_mais_vendido():
    contador_pratos = {}

    for pedido in pedidos:
        for item in pedido["itens"]:
            prato = item["prato"]
            if prato in contador_pratos:
                contador_pratos[prato] += 1
            else:
                contador_pratos[prato] = 1

    prato_popular = ""
    maior_quantidade = 0

    for prato, quantidade in contador_pratos.items():
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            prato_popular = prato

    return prato_popular


resultado = valor_total_gasto()
print(f"Total gasto: R$ {resultado}")
print()
print(f"Prato mais vendido: {prato_mais_vendido()}")
print()


print("=== Top gastadores do dia ===")


gastos_clientes = []
for pedido in pedidos:
    nome = pedido["cliente"]

    total = 0
    for item in pedido["itens"]:
        total += item["preco"]
    gastos_clientes.append([nome, total])


for i in range(len(gastos_clientes)):
    for j in range(i + 1, len(gastos_clientes)):
        if gastos_clientes[i][1] < gastos_clientes[j][1]:
            gastos_clientes[i], gastos_clientes[j] = (
                gastos_clientes[j],
                gastos_clientes[i],
            )


for i in range(min(3, len(gastos_clientes))):
    posicao = i + 1
    nome = gastos_clientes[i][0]
    total = gastos_clientes[i][1]
    print(f"{posicao}º lugar: {nome} - R$ {total}")
