# 1. Faça um programa que leia dois números e mostre qual é o maior.

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
if(n1 > n2):
    print("O Primeiro numero é maior que o segundo:", n1)
elif(n1 == n2):
    print("Os dois números são iguais")
else:
    print("O Segundo numero é maior que o primeiro:", n2)