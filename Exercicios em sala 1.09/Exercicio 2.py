# Estudo de Caso : Cadastro de Produtos
# Um supermercado deseja armazenar informações sobre seus produtos. Cada produto deve
# conter: nome, preço e quantidade em estoque. 
# Utilize um dicionário para representar e manipular essas informações.
# Exemplo:
#produto = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
#print(f"O produto {produto["nome"]} custa R${produto["preco"]}")


produtos =[]
def cadastrar_produto(nome, preco, estoque):
   produto = {"nome": nome, "preco": preco, "estoque": estoque}
   produtos.append(produto)
   print(f"Produto {nome} foi Cadastrado com Sucesso!")

def exibir_produtos():
    if len(produtos) == 0:
        print("Nenhum produto Cadastrado!")
        return
    
    print("\n--- Produtos Cadastrados ---")
    for produto in produtos:
        print(f"nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Estoque: {produto['estoque']}Unidades")

def buscar_produto(nome):
    for produto in produtos:
        if produto["nome"] == nome:
            return produto
    return None

def atualizar_estoque(nome, nova_quantidade):
    produto = buscar_produto(nome)
    if produto:
        produto["estoque"] = nova_quantidade
        print(f"Estoque de {nome} atualizado para {nova_quantidade}")
    else:
        print(f"Produto {nome} Não foi Encontrado!")

def vender_produto(nome, quantidade):
    produto = buscar_produto(nome)
    if produto:
        if produto["estoque"] >= quantidade:
            produto["estoque"] -= quantidade
            total = produto ["preco"] * quantidade
            print(f"Venda realizada: {quantidade} unidades de {nome}")
            print(f"total: R$ {total: .2f}")
            print(f"Estoque restante: {produto['estoque']}")
        else:
            print(f"Estoque Insuficiente! Disponivel: {produto['estoque']}")
    else:
        print(f"Produto {nome} Não encontrado!")

print("\n --- Cadastrando Produtos ---")
cadastrar_produto("Arroz", 25.90, 100)
cadastrar_produto("Feijão", 29.99, 150)
cadastrar_produto("Batata", 6.90, 300)            

exibir_produtos()

print("\n --- Operações ---")
vender_produto("Arroz", 10)
atualizar_estoque("Feijão", 75)

print("\n --- Estado Final ---")

exibir_produtos()