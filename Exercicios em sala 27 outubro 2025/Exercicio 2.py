# 2.Capturando exceções múltiplas: Crie um programa que peça ao usuário o nome de uma cor 
# e mostre seu valor em RGB de acordo com um dicionário pré-definido. 
# O programa deve tratar exceções caso o nome da cor não exista no dicionário.

def verificar_cor():
    cores = {
        'vermelho': (255 , 0, 0),
        'verde': (0, 255, 0),
        'azul': (0, 0, 255)
    }

    try: 
        nome_cor = input("Digite o nome de uma cor: ").lower()
        rgb = cores[nome_cor]
        print(f"Valor RGB de {nome_cor}: {rgb}")
    
    except KeyError:
        print(f"Erro: a cor {nome_cor} não existe")

verificar_cor()