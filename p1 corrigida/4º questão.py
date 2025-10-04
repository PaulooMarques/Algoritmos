# 4. A empresa TPVFR (Todo Programador Vai Ficar Rico) deseja conceder
# aumento salarial aos seus programadores. O aumento será calculado
# conforme o salário atual do programador, de acordo com as seguintes regras:
# (A). Salários até R$ 2800,00: aumento de 20%.
# (B). Salários entre R$ 2800,01 e R$ 7000,00: aumento de 15%.
# (C). Salários entre R$ 7000,01 e R$ 15000,00: aumento de 10%.
# (D). Salários acima de R$ 15000,00: aumento de 5%.
# Escreva um programa que recebe o salário de um programador e calcula
# o salário atualizado com o aumento.

def calcular_aumento_salario(salario):
    if salario <= 2800.00:
        aumento_percentual = 20
    elif salario <= 7000.00:
        aumento_percentual = 15
    elif salario <= 15000.00:
        aumento_percentual = 10
    else:
        aumento_percentual = 5
    
    aumento_valor = salario * (aumento_percentual / 100)
    salario_atualizado = salario + aumento_valor
    
    return aumento_percentual, aumento_valor, salario_atualizado


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

while True:
    entrada = input("Digite o salário do programador: R$ ")
    salario = validar_salario(entrada)
    if salario is not None:
        break

percentual, aumento_valor, salario_atualizado = calcular_aumento_salario(salario)

print(f"\nSalário Atual: R$ {salario:.2f}")
print(f"Percentual de Aumento: {percentual}%")
print(f"Valor do Aumento: R$ {aumento_valor:.2f}")
print(f"Salário Após o Aumento: R$ {salario_atualizado:.2f}")