# 4. Desenvolva um programa que leia uma lista de números e mostre a média deles.

entrada = input("digite os numeros separadamente ->")

numeros = [int(x) for x in entrada.split()]

media = sum(numeros) / len(numeros)

print(f"A sua Media de numeros é. {numeros}")