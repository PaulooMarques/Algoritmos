# Caso2: Distâncias em Km
# 1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
# 2. Calcule a distância total percorrida.
# 3. Mostre a maior e a menor distância.
# 4. Calcule a média das distâncias arredondada para cima (use math.ceil).

import math

distancias = []
for i in range(6):
    dist = float(input(f"Distância de viagem {i+1} (km): "))
    distancias.append(dist)

total = sum(distancias)

maior = max(distancias)
menor = min(distancias)

media_arredondada = math.ceil(sum(distancias) / 6)

print(f"\nDistâncias: {distancias}")
print(f"Total: {total} km")
print(f"Maior: {maior} km | Menor: {menor} km")
print(f"Média (arredondada): {media_arredondada} km")
