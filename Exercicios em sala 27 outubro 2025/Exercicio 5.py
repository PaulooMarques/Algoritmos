# 5.Simulação de transações: Crie um programa que simule uma transferência bancária. 
# Peça ao usuário o saldo da conta e o valor da transferência. Caso o saldo seja insuficiente, 
# levante uma exceção do tipo ValueError com a mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o usuário.

class SaldoInsuficienteError(Exception):
    pass

def simular_transferencia():
    try:
        saldo = float(input("Digite o saldo da conta: R$ "))
        valor_transferencia = float(input("Digite o valor da transferência: R$ "))
        
        if valor_transferencia > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar a transferência!")
        
        novo_saldo = saldo - valor_transferencia
        print(f"Transferência realizada com sucesso!")
        print(f"Saldo anterior: R$ {saldo:.2f}")
        print(f"Valor transferido: R$ {valor_transferencia:.2f}")
        print(f"Novo saldo: R$ {novo_saldo:.2f}")
        
    except ValueError:
        print("Digite apenas valores numéricos!")
    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")
    finally:
        print("\n Operação finalizada.")

simular_transferencia()