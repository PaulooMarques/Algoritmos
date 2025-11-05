# 4.Exceções personalizadas: Escreva uma função que verifica se uma senha possui no mínimo 8 caracteres e pelo menos um número. 
# Se a senha não atender aos requisitos, levante uma exceção com uma mensagem personalizada. 
# Trate a exceção e mostre a mensagem ao usuário.

class SenhaInvalidaError(Exception):
    pass

def verificar_senha():
    try:
        senha = input("Digite uma senha (minimo 8 caracteres): ")
        
        if len(senha) < 8:
            raise SenhaInvalidaError("A senha deve ter no minimo 8 caracteres")
        
        print("Senha Valida: Cadastro com Sucesso")
    
    except SenhaInvalidaError as e:
        print(f"Erro: {e}")

verificar_senha()