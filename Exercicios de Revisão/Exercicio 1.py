# 1.Cálculo de Complexidade Simples Escreva um algoritmo que conte quantas operações básicas (somas) são executadas para calcular a soma dos números de 1 até n.
# Exiba o resultado e compare com a fórmula matemática n*(n+1)/2.


def soma_iterativa(n):

    soma = 0
    operacoes = 0

    for i in range(1, n + 1):
        soma += i
        operacoes += 1

    return soma, operacoes


def soma_formula(n):

    return n * (n + 1) // 2


# Testando com diferentes valores
valores = [10, 100, 1000]

print("n\tIterativo\tFórmula\t\tOperações")
print("-" * 40)

for n in valores:
    resultado_iter, ops = soma_iterativa(n)
    resultado_form = soma_formula(n)

    print(f"{n}\t{resultado_iter}\t\t{resultado_form}\t\t{ops}")

# Comparação de complexidade
print("\nComplexidade:")
print("Iterativo: O(n) - cresce linearmente")
print("Fórmula: O(1) - sempre constante")

# Exemplo visual pequeno
n = 5
soma, ops = soma_iterativa(n)
formula = soma_formula(n)

print(f"\nPara n={n}:")
print(f"Iterativo: {ops} operações → {soma}")
print(f"Fórmula: 1 operação → {formula}")
