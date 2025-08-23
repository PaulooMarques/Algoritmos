def sistema_login():

    senha_correta = "senha123"
    max_tentativas = 3
    tentativa = 0

    print("=== SISTEMA DE LOGIN ===")

    while tentativa < max_tentativas:
        tentativa += 1
        senha_digitada = input(f"Tentativa {tentativa}/3 - Digite a senha: ")

        if senha_digitada == senha_correta:
            print("Bem-vindo!")
            return True
        else:
            if tentativa < max_tentativas:
                restantes = max_tentativas - tentativa
                print(f"Senha incorreta! {restantes} tentativa(s) restante(s).")
            else:
                print("Acesso Negado!")
                return False

    return False


def reiniciar_sistema():

    while True:
        sucesso = sistema_login()

        if sucesso:
            print("Sessão encerrada.")
            break
        else:
            # Pergunta se quer tentar novamente caso falar as 3 tentativas.
            # caso digitar sim a def reinicia, caso digitar não ela se encerra.
            resposta = input("\nDeseja tentar novamente? (s/n): ").lower()
            if resposta != "s":
                print("Sistema encerrado.")
                break
            print("\n--- REINICIANDO SISTEMA ---\n")


if __name__ == "__main__":
    reiniciar_sistema()
