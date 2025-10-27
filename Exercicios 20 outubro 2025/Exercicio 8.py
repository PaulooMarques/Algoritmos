# 8. Distribuição de Cadeiras
# Contexto: Uma sala de cinema tem 5 filas com 6 cadeiras cada.
# Tarefa: Crie uma matriz 5x6 e marque quais cadeiras estão ocupadas com “X” e quais estão
# livres com “O”.

cinema = [
    ["X", "X", "O", "O", "X", "O"],
    ["X", "O", "O", "X", "X", "X"],
    ["O", "O", "O", "O", "O", "O"],
    ["X", "X", "X", "X", "O", "O"],
    ["X", "X", "X", "X", "X", "X"]
]

filas = ["A", "B", "C", "D", "E"]

print("=" * 60)
print("CINEMA ESTRELA - MAPA DE ASSENTOS")
print("=" * 60)
print("\n               [ TELA ]")
print()

print("      ", end="")
for i in range(1, 7):
    print(f"  {i} ", end="")
print("\n")

for i in range(len(cinema)):
    print(f"Fila {filas[i]}  ", end="")
    for j in range(len(cinema[i])):
        if cinema[i][j] == "X":
            print(" [X]", end="")
        else:
            print(" [ ]", end="")
    print()

print("\nLegenda: [X] = Ocupado  [ ] = Livre")

print("\n" + "=" * 60)
print("ESTATÍSTICAS DE OCUPAÇÃO")
print("=" * 60)

total_assentos = len(cinema) * len(cinema[0])
assentos_ocupados = 0
assentos_livres = 0

for fila in cinema:
    for cadeira in fila:
        if cadeira == "X":
            assentos_ocupados += 1
        else:
            assentos_livres += 1

taxa_ocupacao = (assentos_ocupados / total_assentos) * 100

print(f"\nTotal de assentos: {total_assentos}")
print(f"Assentos ocupados: {assentos_ocupados}")
print(f"Assentos disponíveis: {assentos_livres}")
print(f"Taxa de ocupação: {taxa_ocupacao:.1f}%")

print("\n" + "=" * 60)
print("OCUPAÇÃO POR FILA")
print("=" * 60)

for i in range(len(cinema)):
    ocupados_fila = cinema[i].count("X")
    livres_fila = cinema[i].count("O")
    taxa_fila = (ocupados_fila / len(cinema[i])) * 100
    
    status = ""
    if ocupados_fila == len(cinema[i]):
        status = "LOTADA"
    elif ocupados_fila == 0:
        status = "VAZIA"
    else:
        status = f"{taxa_fila:.0f}% ocupada"
    
    print(f"Fila {filas[i]}: {ocupados_fila} ocupados, {livres_fila} livres - {status}")

print("\n" + "=" * 60)
print("ASSENTOS DISPONÍVEIS PARA RESERVA")
print("=" * 60)

assentos_disponiveis = []
for i in range(len(cinema)):
    for j in range(len(cinema[i])):
        if cinema[i][j] == "O":
            assentos_disponiveis.append(f"{filas[i]}{j+1}")

if assentos_disponiveis:
    print("\nAssentos livres:", ", ".join(assentos_disponiveis))
else:
    print("\nSessão esgotada! Não há assentos disponíveis.")

print("\n" + "=" * 60)
print("SISTEMA DE RESERVA")
print("=" * 60)

while True:
    opcao = input("\nDeseja reservar um assento? (S/N): ").strip().upper()
    
    if opcao == "N":
        print("\n✓ Obrigado por utilizar nosso sistema!")
        break
    elif opcao == "S":
        if assentos_livres == 0:
            print("Desculpe, não há mais assentos disponíveis!")
            break
        
        fila_escolhida = input("Digite a fila (A-E): ").strip().upper()
        
        if fila_escolhida not in filas:
            print("Fila inválida! Escolha entre A e E.")
            continue
        
        try:
            cadeira_escolhida = int(input("Digite o número da cadeira (1-6): "))
            
            if cadeira_escolhida < 1 or cadeira_escolhida > 6:
                print("Número de cadeira inválido! Escolha entre 1 e 6.")
                continue
            
            indice_fila = filas.index(fila_escolhida)
            indice_cadeira = cadeira_escolhida - 1
            
            if cinema[indice_fila][indice_cadeira] == "X":
                print(f"Assento {fila_escolhida}{cadeira_escolhida} já está ocupado!")
            else:
                cinema[indice_fila][indice_cadeira] = "X"
                assentos_livres -= 1
                print(f"Assento {fila_escolhida}{cadeira_escolhida} reservado com sucesso!")
                print(f"Assentos disponíveis restantes: {assentos_livres}")
                
        except ValueError:
            print("Digite apenas números para a cadeira!")
    else:
        print("Opção inválida! Digite S para Sim ou N para Não.")

print("=" * 60)