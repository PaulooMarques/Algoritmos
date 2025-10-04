# 1. Escreva um programa em Python que tenha uma função chamada
# calcular_media_notas. Esta função deve receber uma lista de notas de um aluno
# e calcular a média dessas notas. O programa principal deve:
# (A). Solicitar ao usuário que informe o nome do aluno.
# (B). Solicitar ao usuário que informe as notas do aluno (o número de
# notas pode ser variável, mas o programa deve permitir que o usuário
# adicione pelo menos 5 notas).
# (C). Chamar a função calcular_media_notas passando a lista de notas
# e exibir a média das notas.
# (D). Caso a média seja superior ou igual a 7, exibir que o aluno foi
# aprovado. Caso contrário, exibir que o aluno foi reprovado.

def calcular_media_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)


def validar_nota(nota_str):
    try:
        nota = float(nota_str)
        if 0 <= nota <= 10:
            return nota
        else:
            print("A nota deve estar entre 0 e 10!")
            return None
    except ValueError:
        print("Digite um número válido!")
        return None


nome_aluno = input("Digite o nome do aluno: ")

lista_notas = []
print("\nDigite as notas do aluno (mínimo de 5 notas).")
print("Digite 'fim' quando terminar de adicionar notas.\n")

contador = 1
while True:
    entrada = input(f"Digite a {contador}ª nota (ou 'fim' para encerrar): ")
    
    if entrada.lower() == 'fim':
        if len(lista_notas) < 5:
            print(f"Você precisa adicionar pelo menos 5 notas. Você tem {len(lista_notas)}.")
            continue
        else:
            break
    
    nota = validar_nota(entrada)
    if nota is not None:
        lista_notas.append(nota)
        contador += 1

media = calcular_media_notas(lista_notas)
print(f"\n{'='*50}")
print(f"Aluno: {nome_aluno}")
print(f"Notas: {lista_notas}")
print(f"Média: {media:.2f}")

if media >= 7:
    print(f"Resultado: {nome_aluno} foi APROVADO!")
else:
    print(f"Resultado: {nome_aluno} foi REPROVADO.")
print(f"{'='*50}")