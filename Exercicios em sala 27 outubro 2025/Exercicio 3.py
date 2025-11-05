# 3.Bloco else e finally: Escreva um programa que solicite um número ao usuário. 
# Se o número for maior que 10, exiba uma mensagem dizendo que o número é válido. 
# Utilize o bloco else para imprimir que o programa foi executado com sucesso, e o bloco finally para imprimir "Programa encerrado".

def validar_numero():
    try:
        numero = int(input("Digite um numero: "))

        if numero >= 10:
            print("O numero é valido!")
        else:
            print("O numero deve ser Maior que 10!!")
    
    except ValueError:
        print(" Voce Deve digitar um numero inteiro!")
    else:
        print(" Programa Executado com Sucesso!!")
    finally:
        print("Programa encerrado.")

validar_numero()