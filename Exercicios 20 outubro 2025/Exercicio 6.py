# 6. Horários de Transporte
# Contexto: Um ponto de ônibus tem 4 linhas, cada uma com 3 horários.
# Tarefa: Armazene os horários em uma matriz 4x3 e permita que o usuário consulte os horários
# de uma linha específica.

horarios = [
    ["06:30", "12:00", "18:30"],
    ["07:00", "13:30", "19:00"],
    ["06:45", "12:30", "18:00"],
    ["07:15", "14:00", "20:00"]
]

linhas = [
    "Linha 101 - Centro/Praia",
    "Linha 205 - Shopping/Hospital", 
    "Linha 310 - Universidade/Rodoviária",
    "Linha 425 - Aeroporto/Centro"
]

periodos = ["Manhã", "Tarde", "Noite"]

print("=" * 70)
print("SISTEMA DE TRANSPORTE PÚBLICO - HORÁRIOS")
print("=" * 70)

print("\nTodos os horários disponíveis:\n")

for i in range(len(horarios)):
    print(f"{linhas[i]}")
    print("-" * 70)
    for j in range(len(horarios[i])):
        print(f"   {periodos[j]}: {horarios[i][j]}")
    print()

print("=" * 70)
print("CONSULTAR HORÁRIOS POR LINHA")
print("=" * 70)
print("\nLinhas disponíveis:")

for i in range(len(linhas)):
    print(f"{i + 1} - {linhas[i]}")

print("0 - Sair")

while True:
    print("\n" + "-" * 70)
    try:
        opcao = int(input("\nDigite o número da linha para consultar (0 para sair): "))
        
        if opcao == 0:
            print("\n✓ Encerrando consulta. Boa viagem!")
            break
        elif 1 <= opcao <= len(linhas):
            indice = opcao - 1
            print("\n" + "=" * 70)
            print(f"{linhas[indice]}")
            print("=" * 70)
            print("\nHorários de partida:")
            
            for j in range(len(horarios[indice])):
                print(f"  • {periodos[j]}: {horarios[indice][j]}")
            
            print("\nDica: Chegue com 5 minutos de antecedência!")
            
        else:
            print("Opção inválida! Escolha uma linha entre 1 e 4.")
            
    except ValueError:
        print("Por favor, digite apenas números!")
    except KeyboardInterrupt:
        print("\n\n✓ Consulta interrompida. Até logo!")
        break

print("=" * 70)