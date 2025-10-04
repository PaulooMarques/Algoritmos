# Escreva um programa em Python que contenha uma função chamada
# calcula_bonificacao.
# (A). Essa função deve receber dois parâmetros:
# i. taxa_bonus: A porcentagem de bonificação de produção
# concedida ao funcionário.
# ii. salario_base: O salário do funcionário antes da bonificação.
# A função deve calcular e retornar o novo salário do funcionário, já
# incluindo a bonificação. No programa principal, solicite ao usuário que
# informe o salário base e a taxa de bonificação, chame a função e exiba o
# salário final, a bonificação concedida e o salário base informado.

def calcula_bonificacao(taxa_bonus, salario_base):
    bonificacao = salario_base * (taxa_bonus / 100)
    novo_salario = salario_base + bonificacao
    return bonificacao, novo_salario


def validar_salario(valor_str):
    try:
        valor = float(valor_str)
        if valor > 0:
            return valor
        else:
            print("O salário deve ser maior que zero!")
            return None
    except ValueError:
        print("Digite um valor numérico válido!")
        return None


def validar_taxa_bonus(taxa_str):
    try:
        taxa = float(taxa_str)
        if 0 <= taxa <= 100:
            return taxa
        else:
            print("A taxa de bonificação deve estar entre 0 e 100%!")
            return None
    except ValueError:
        print("Digite um valor numérico válido!")
        return None

print("=" * 60)
print("CALCULADORA DE BONIFICAÇÃO DE FUNCIONÁRIOS")
print("=" * 60)

while True:
    entrada_salario = input("\nInforme o salário base do funcionário: R$ ")
    salario_base = validar_salario(entrada_salario)
    if salario_base is not None:
        break

while True:
    entrada_taxa = input("Informe a taxa de bonificação (%): ")
    taxa_bonus = validar_taxa_bonus(entrada_taxa)
    if taxa_bonus is not None:
        break

bonificacao_concedida, novo_salario = calcula_bonificacao(taxa_bonus, salario_base)

print("\n" + "=" * 60)
print("RESULTADO DO CÁLCULO")
print("=" * 60)
print(f"Salário Base informado:    R$ {salario_base:>10,.2f}")
print(f"Taxa de Bonificação:          {taxa_bonus:>10.2f}%")
print(f"Bonificação Concedida:     R$ {bonificacao_concedida:>10,.2f}")
print("-" * 60)
print(f"Salário Final:             R$ {novo_salario:>10,.2f}")
print("=" * 60)

percentual_aumento = (bonificacao_concedida / salario_base) * 100
print(f"\nO salário teve um aumento de {percentual_aumento:.2f}%")
print(f"Isso representa R$ {bonificacao_concedida:,.2f} a mais por mês.")