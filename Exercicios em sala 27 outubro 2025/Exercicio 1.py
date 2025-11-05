# 1.Tratamento de exceções básicas: Escreva um programa que peça ao usuário dois números e faça a divisão do primeiro pelo segundo. 
# Se o usuário inserir um valor inválido ou tentar dividir por zero, o programa deve exibir uma mensagem de erro apropriada.


def divisão_segura():
    try:
        num1 = float(input("Digite o Primeiro Numero: "))
        num2 = float(input("Digite o Segundo Numero: "))


        resultado = num1 / num2
        print(f"O Resultado é {resultado}")

    except ZeroDivisionError:
        print("Erro, é possivel dividir por 0")
    except ValueError:
        print("ERRO: Insira Numeros Validos")

divisão_segura()