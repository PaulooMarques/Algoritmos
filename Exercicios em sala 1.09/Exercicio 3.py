# Estudo de Caso 2: Agenda Telefônica
# Uma agenda pode ser representada como um dicionário em que as chaves são os nomes
# das pessoas e os valores são os números de telefone.
# Exemplo:
# agenda = {"Maria": "99999-1234", "João": "98888-5678"}
# print("Telefone da Maria:", agenda["Maria"])

agenda = {}

def cadastrar_contato(nome, telefone):
    agenda[nome] = telefone
    print(f"Contato {nome} cadastrado com sucesso!")

def exibir_contatos():
    if not agenda:
        print("Agenda vazia!")
        return
    print("\n--- Contatos na Agenda ---")
    for nome, telefone in agenda.items():
        print(f"{nome}: {telefone}")

def buscar_telefone(nome):
    telefone = agenda.get(nome)
    if telefone:
        print(f"Telefone de {nome}: {telefone}")
    else:
        print(f"Contato {nome} não encontrado!")

def atualizar_telefone(nome, novo_telefone):
    if nome in agenda:
        agenda[nome] = novo_telefone
        print(f"Telefone de {nome} atualizado para {novo_telefone}")
    else:
        print(f"Contato {nome} não encontrado!")

def apagar_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} apagado da agenda.")
    else:
        print(f"Contato {nome} não encontrado!")


cadastrar_contato("Maria", "99999-1234")
cadastrar_contato("João", "98888-5678")
exibir_contatos()
buscar_telefone("Maria")
atualizar_telefone("João", "97777-4321")
apagar_contato("Maria")
exibir_contatos()
