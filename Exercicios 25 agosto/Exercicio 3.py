estoque = [
    ["Arroz", 50, 5.90],
    ["Feijão", 3, 8.50], 
    ["Açúcar", 25, 4.20],
    ["Óleo", 2, 6.80],
    ["Café", 1, 12.50]
]


total_estoque = sum(qtd * preco for nome, qtd, preco in estoque)


maior_valor = 0
produto_maior = ""
for nome, qtd, preco in estoque:
    valor = qtd * preco
    if valor > maior_valor:
        maior_valor = valor
        produto_maior = nome


estoque_baixo = []
for nome, qtd, preco in estoque:
    if qtd < 5:
        estoque_baixo.append(nome)


print("=== PRODUTOS EM ESTOQUE ===")
for i, (nome, qtd, preco) in enumerate(estoque, 1):
    print(f"{i}. {nome} - Qtd: {qtd} - R$ {preco:.2f}")

print(f"\n1. Valor total: R$ {total_estoque:.2f}")
print(f"2. Maior valor: {produto_maior} (R$ {maior_valor:.2f})")
print(f"3. Estoque baixo: {estoque_baixo}")

# 4. Buscar produto com input
print("\n=== BUSCA DE PRODUTO ===")
nome_busca = input("Digite o nome do produto: ")

produto_encontrado = None
for produto in estoque:
    if produto[0].lower() == nome_busca.lower():
        produto_encontrado = produto
        break

if produto_encontrado:
    nome, qtd, preco = produto_encontrado
    print(f"✓ Produto: {nome} | Qtd: {qtd} | Preço: R$ {preco:.2f} | Total: R$ {qtd*preco:.2f}")
else:
    print(f"✗ Produto '{nome_busca}' não encontrado")


# Versão ultra-compacta com list comprehension:
# total = sum(q*p for n,q,p in estoque)
# maior = max(estoque, key=lambda x: x[1]*x[2])
# baixo = [n for n,q,p in estoque if q < 5]