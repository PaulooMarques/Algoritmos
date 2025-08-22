# 2. Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.


num = input("Digite um número: ")
for x in range(1, 11):
    print(f"Tabuada {num}x{x}:", float(num) * x)