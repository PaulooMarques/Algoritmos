# 3. Crie um programa em Python que implemente uma função chamada
# calcula_imposto_renda. A função deve receber um único parâmetro:
# salário: o valor do salário bruto de um indivíduo.
# Curso de Graduação em Engenharia de Software
# Algoritmos
# Com base na tabela de alíquotas abaixo, a função deve calcular e
# retornar o valor do imposto de renda devido:
# Faixa Salarial (R$) Alíquota (%) Dedução (R$) Faixa Salarial (R$)
# Até 2.112,00 Isento 0 Até 2.112,01
# De 2.112,01 a 2.826,65 7,50% 158,4 De 2.112,01 a 2.826,66
# De 2.826,66 a 3.751,05 15% 370,4 De 2.826,66 a 3.751,06
# De 3.751,06 a 4.664,68 22,50% 651,73 De 3.751,06 a 4.664,69
# Acima de 4.664,68 27,50% 884,96 Acima de 4.664,69
# Requisitos:
# • A função deve retornar o valor do imposto de renda a ser pago.
# • O programa deve solicitar ao usuário o salário bruto, chamar a função e
# exibir o imposto devido.


def calcula_imposto_renda(salario):
    if salario <= 2112.00:
        imposto = 0
        aliquota = 0
        faixa = "Isento"
    elif salario <= 2826.65:
        imposto = salario * 0.075 - 158.40
        aliquota = 7.5
        faixa = "De R$ 2.112,01 a R$ 2.826,65"
    elif salario <= 3751.05:
        imposto = salario * 0.15 - 370.40
        aliquota = 15.0
        faixa = "De R$ 2.826,66 a R$ 3.751,05"
    elif salario <= 4664.68:
        imposto = salario * 0.225 - 651.73
        aliquota = 22.5
        faixa = "De R$ 3.751,06 a R$ 4.664,68"
    else:
        imposto = salario * 0.275 - 884.96
        aliquota = 27.5
        faixa = "Acima de R$ 4.664,68"
    
    return imposto, aliquota, faixa


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


def exibir_tabela_ir():
    print("\n" + "=" * 70)
    print("Tabela de Imposto de Renda")
    print("=" * 70)
    print(f"{'Faixa Salarial':<30} {'Alíquota':<12} {'Dedução':<15}")
    print("-" * 70)
    print(f"{'Até R$ 2.112,00':<30} {'Isento':<12} {'R$ 0,00':<15}")
    print(f"{'De R$ 2.112,01 a R$ 2.826,65':<30} {'7,50%':<12} {'R$ 158,40':<15}")
    print(f"{'De R$ 2.826,66 a R$ 3.751,05':<30} {'15,00%':<12} {'R$ 370,40':<15}")
    print(f"{'De R$ 3.751,06 a R$ 4.664,68':<30} {'22,50%':<12} {'R$ 651,73':<15}")
    print(f"{'Acima de R$ 4.664,68':<30} {'27,50%':<12} {'R$ 884,96':<15}")
    print("=" * 70 + "\n")


print("=" * 70)
print("Calculo de Imposto de Renda")
print("=" * 70)

mostrar_tabela = input("Deseja visualizar a tabela de IR? (s/n): ").lower()
if mostrar_tabela == 's':
    exibir_tabela_ir()

while True:
    entrada_salario = input("Digite o salário bruto: R$ ")
    salario = validar_salario(entrada_salario)
    if salario is not None:
        break

imposto_devido, aliquota_aplicada, faixa_salarial = calcula_imposto_renda(salario)

salario_liquido = salario - imposto_devido


print("\n" + "=" * 70)
print("Resultado do Cálculo de Imposto")
print("=" * 70)
print(f"Salário Bruto:              R$ {salario:>12,.2f}")
print(f"Faixa Salarial:             {faixa_salarial}")
print(f"Alíquota Aplicada:          {aliquota_aplicada:>12.2f}%")
print(f"Imposto de Renda Devido:    R$ {imposto_devido:>12,.2f}")
print("-" * 70)
print(f"Salário Líquido:            R$ {salario_liquido:>12,.2f}")
print("=" * 70)

if imposto_devido > 0:
    percentual_desconto = (imposto_devido / salario) * 100
    print(f"\nO imposto representa {percentual_desconto:.2f}% do seu salário bruto.")
    print(f"Desconto mensal: R$ {imposto_devido:,.2f}")
    print(f"Desconto anual:  R$ {imposto_devido * 12:,.2f}")
else:
    print("\nParabéns! Você está isento de Imposto de Renda.")