# 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Em seguida, exiba apenas o nome do aluno.

aluno = {"nome": "Paulo", "idade": 24, "curso": "Engenharia de Software"}

print("Nome do Aluno:", aluno["nome"])

# 2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
# Depois, remova a chave "idade".

aluno["nota"] = 9.5
del aluno["idade"]
print("Dicionário após adicionar nota e remover idade:", aluno)


# 3. Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço:
# produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}
print("\nProdutos e Seus Preços:")
for produto, preço in produtos.items():
    print(f"{produto}: R$ {preço}")


# 4. Dado o dicionário aluno, verifique se existe a chave "curso".

if "curso" in aluno:
    print("\nA Chave 'curso' existe no dicionário aluno")
else:
    print("\nA Chave 'curso' não existe no dicionário aluno")

# 5. Crie um dicionário chamado turma que contenha dois alunos, cada um com nome
# e nota.
# Depois, exiba o nome do primeiro aluno e a nota do segundo aluno.

turma = {
    "aluno1": {"nome": "Wilker", "nota": 9.2},
    "aluno2": {"nome": "Pedro", "nota": 6.5},
}
print(f"\nNome do primeiro aluno:{turma['aluno1']['nome']}")
print(f"\nNota do segundo aluno:{turma['aluno2']['nota']}")
# 6. Crie um dicionário representando um carro com as chaves: marca, modelo e ano.
# a. Adicione ao dicionário do carro a chave 'cor'.

carro = {"marca": "BMW", "modelo": "M3 GTR", "ano": 2005}

carro["cor"] = "Prata"
print(f"\nCarro após adicionar cor: {carro}")
# b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como valor).

notas = {"Jorge": 9.1, "Sidney": 5.5, "Thiago": 6.9}

print(f"\nDicionário de notas: {notas}")
# c. Acesse a nota de um dos alunos e exiba.
print(f"Nota do Jorge: {notas['Jorge']}")
# d. Remova um aluno do dicionário de notas.
del notas["Sidney"]
print(f"Dicionário após remover o Sidney: {notas}")
