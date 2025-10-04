# 5. Você deve criar um programa em Python que utilize um dicionário para
# armazenar as informações de funcionários de uma empresa. O programa
# deve ser capaz de fazer o seguinte:
# (A) Perguntar o nome, o salário e o cargo de cada funcionário.
# (B) Armazenar essas informações em um dicionário, onde a chave
# será o nome do funcionário e o valor será outro dicionário com
# as informações de salário e cargo.
# (C)O programa deve permitir ao usuário consultar o salário e o
# cargo de um funcionário informando seu nome.
# (D)O programa também deve permitir que o usuário liste todos os
# funcionários cadastrados, mostrando seu nome, cargo e
# salário.

def validar_nome(nome):
    return nome.strip() != ""


def validar_salario(salario_str):
    try:
        salario = float(salario_str)
        return salario > 0
    except ValueError:
        return False


def adicionar_funcionario(funcionarios):
    while True:
        nome = input("Digite o nome do Funcionário: ").strip()
        if not validar_nome(nome):
            print("O nome não pode estar vazio!")
            continue
        
        if nome in funcionarios:
            print(f"Funcionário '{nome}' já está cadastrado!")
            sobrescrever = input("Deseja atualizar os dados? (s/n): ").lower()
            if sobrescrever != 's':
                return
        break
    
    while True:
        salario_str = input("Digite o Salário: R$ ")
        if validar_salario(salario_str):
            salario = float(salario_str)
            break
        else:
            print("O salário deve ser um valor positivo!")
    
    cargo = input("Digite o Cargo: ").strip()
    
    funcionarios[nome] = {"salario": salario, "cargo": cargo}
    print(f"Funcionário {nome} adicionado com Sucesso!")


def consultar_funcionario(funcionarios):
    nome = input("Digite o nome do Funcionário para Consultar os seus dados: ").strip()
    if nome in funcionarios:
        print(f"Nome: {nome}")
        print(f"Cargo: {funcionarios[nome]['cargo']}")
        print(f"Salário: R$ {funcionarios[nome]['salario']:.2f}")
        print("-" * 30)
    else:
        print("Funcionário Não Encontrado.")
        print("-" * 30)


def listar_funcionarios(funcionarios):
    if funcionarios:
        print("\n --- Lista de Funcionários ---")
        for nome, info in funcionarios.items():
            print(f"Nome: {nome}")
            print(f"Cargo: {info['cargo']}")
            print(f"Salário: R$ {info['salario']:.2f}")
            print("-" * 30)
    else:
        print("Nenhum Funcionário Cadastrado.")
        print("-" * 30)


funcionarios = {}

while True:
    print("\n1. Adicionar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Listar todos os Funcionários")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_funcionario(funcionarios)
    elif opcao == "2":
        consultar_funcionario(funcionarios)
    elif opcao == "3":
        listar_funcionarios(funcionarios)
    elif opcao == "4":
        print("Encerrando Programa.")
        break
    else:
        print("Opção Inválida: Tente Novamente.")