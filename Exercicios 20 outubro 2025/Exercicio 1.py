# 1. Controle de Temperatura de Salas
# Contexto: Uma empresa monitora a temperatura de 5 salas, 3 vezes ao dia.
# Tarefa: Armazene as temperaturas em uma matriz 5x3. Calcule a temperatura média de cada
# sala.

temperaturas = [
    [22.5, 24.0, 23.2],  
    [21.8, 23.5, 22.9],  
    [25.1, 26.3, 25.7],  
    [20.5, 22.1, 21.3],  
    [23.7, 25.2, 24.5]   
]

print("\nTemperaturas registradas (°C):")
print("\nSala\tManhã\tTarde\tNoite")
print("-" * 40)

for i in range(len(temperaturas)):
    print(f"Sala {i+1}\t{temperaturas[i][0]}\t{temperaturas[i][1]}\t{temperaturas[i][2]}")

print("\n" + "=" * 50)
print("Média de Temperatura por Sala")
print("=" * 50)

for i in range(len(temperaturas)):
    soma = sum(temperaturas[i])
    media = soma / len(temperaturas[i])
    print(f"Sala {i+1}: {media:.2f}°C")

medias_salas = []
for sala in temperaturas:
    medias_salas.append(sum(sala) / len(sala))

sala_mais_quente = medias_salas.index(max(medias_salas)) + 1
sala_mais_fria = medias_salas.index(min(medias_salas)) + 1

print("\n" + "=" * 50)
print(f"Sala mais quente: Sala {sala_mais_quente} ({max(medias_salas):.2f}°C)")
print(f"Sala mais fria: Sala {sala_mais_fria} ({min(medias_salas):.2f}°C)")
print("=" * 50)