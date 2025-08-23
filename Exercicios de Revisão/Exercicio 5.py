# 5. Verificação de CPF (simplificado)
# Peça ao usuário um número de 11 dígitos e:
# • Verifique se todos os caracteres são dígitos;
# • Verifique se o tamanho é válido (11);
# • Mostre "CPF válido" ou "CPF inválido".
# (Não precisa calcular os dígitos verificadores ainda — é apenas validação estrutural.)


def validador_CPF(cpf):

    # Remove espaços em branco
    cpf = cpf.strip()

    # para saber se tem especificamente 11 caracteres
    if len(cpf) != 11:
        return False

    # Verifica se todos os caracteres são dígitos
    if not cpf.isdigit():
        return False

    return True


def sistema_validacao_cpf():
    print("=== VALIDAÇÃO ESTRUTURAL DE CPF ===")
    print("Digite um CPF com 11 dígitos (apenas números)")

    while True:
        cpf = input("\nDigite o CPF (ou 'sair' para encerrar): ")

        if cpf.lower() == "sair":
            print("Encerrando validação.")
            break

        # Realizar validação
        if validador_CPF(cpf):
            print(f"✓ O CPF '{cpf}' é válido.")
        else:
            print(f"✗ CPF '{cpf}' é inválido.")

            cpf_limpo = cpf.strip()
            if len(cpf_limpo) != 11:
                print(f"  → Erro: Deve ter 11 dígitos (tem {len(cpf_limpo)})")
            elif not cpf_limpo.isdigit():
                print("  → Erro: Cpf só contem números")


if __name__ == "__main__":
    sistema_validacao_cpf()
